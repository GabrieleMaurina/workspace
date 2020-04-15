#!/usr/bin/env python3

from os import walk, makedirs
from os.path import join, exists, relpath
from argparse import ArgumentParser as arg_par
from hashlib import sha1
from json import load, dump
from itertools import chain
from collections import deque
from sys import stdout
import subprocess

FOLDER = '.derts'
profiles = {
	'c':{'c','h'},
	'java':{'java'},
	'js':{'js'},
	'lisp':{'lisp', 'lsp'},
	'ml':{'ml'},
	'php':{'php'}
}

def get_profile(language):
	if language in profiles:
		return profiles[language]
	else:
		raise Exception('Language not supported.')

def sha1_file(path):
	with open(path, 'rb') as file:
		return sha1(file.read()).hexdigest()

def load_hashes(path):
	try:
		with open(join(path, FOLDER, 'hashes.json'), 'r') as hashes:
			return load(hashes)
	except:
		return {}

def derts_dir(path):
	path = join(path, FOLDER)
	if not exists(path):
			try:
				makedirs(path)
			except: pass
	return path

def dump_json(path, name, obj):
	with open(join(derts_dir(path), name + '.json'), 'w') as file:
		dump(obj, file)	

def get_files(path, profile):
	for root, dirs, names in walk(path):
		dirs[:] = [d for d in dirs if d[0] != '.']
		for name in names:
			full = join(root, name)
			splt = name.rsplit('.', 1)
			if len(splt) == 2:
				name, ext = splt
				if ext in profile:
					yield full

def get_dependencies_pfff(language, project_folder, dependencies_extractor):
	if not dependencies_extractor: pass
	dependencies_extractor = join('.', dependencies_extractor)
	result = subprocess.run(
		args=[dependencies_extractor, language, project_folder],
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		encoding='utf-8')
	if result.returncode:
		raise Exception('Unable to get dependencies: ' + result.stderr)
	else:
		dependencies = {}
		for line in result.stdout.split('\n'):
			if line:
				file1, file2 = (relpath(value, project_folder) for value in line.split())
				if file1 in dependencies:
					dependencies[file1].append(file2)
				else:
					dependencies[file1] = [file2]
		return dependencies

def dfs_changed(test, dependencies, changed):
	neighbors = deque(dependencies.get(test, []))
	visited = set(test)
	while neighbors:
		neighbor = neighbors.pop()
		if neighbor not in visited:
			visited.add(neighbor)
			if neighbor in changed:
				return True
			elif neighbor in dependencies:
				neighbors.extend(dependencies[neighbor])
	return False

def select(tests, dependencies, changed):
	selected = set()
	for test in tests:
		if test in changed or dfs_changed(test, dependencies, changed):
			selected.add(test)
	return selected

def rts(language, project_folder, test_folder, source_folder, dependencies_extractor):
	profile = get_profile(language)

	test_folder = join(project_folder, test_folder)
	source_folder = join(project_folder, source_folder)

	test_files = [relpath(file, project_folder) for file in get_files(test_folder, profile)]
	source_files = [relpath(file, project_folder) for file in get_files(source_folder, profile)]

	old_hashes = load_hashes(project_folder)
	new_hashes = {file:sha1_file(join(project_folder, file)) for file in chain(test_files, source_files)}

	changed = {file for file, hash in new_hashes.items() if file not in old_hashes or new_hashes[file] != old_hashes[file]}
	dependencies = get_dependencies_pfff(language, project_folder, dependencies_extractor)
	selected = select(test_files, dependencies, changed)	
	
	return selected, dependencies, changed, new_hashes, test_files, source_files

def save_jsons(project_folder, selected, dependencies, changed, new_hashes):
	dump_json(project_folder, 'selected', list(selected))
	dump_json(project_folder, 'dependencies',  dependencies)
	dump_json(project_folder, 'changed',  list(changed))
	dump_json(project_folder, 'hashes',  new_hashes)

def print_results_file(selected, output):
	for test_file in selected:
		print(test_file, file=output)

def print_results(selected, output):
	if output == 'stdout':
		print_results_file(selected, stdout)
	else:
		with open(output, 'w') as output:
			print_results_file(selected, output)

def log(selected, dependencies, changed, test_files, source_files):
	T = len(test_files)
	S = len(source_files)
	C = len(changed)
	D = sum(len(v) for v in dependencies.values())
	SE = len(selected)
	print('***Derts results***\nTest files: {}\nSource files: {}\nChanged: {}\nDependencies: {}\nSelected: {}'.format(T, S, C, D, SE), file=stderr)

def run(language, project_folder, test_folder, source_folder, verbose, output, dependencies_extractor):
	selected, dependencies, changed, new_hashes, test_files, source_files = rts(language, project_folder, test_folder, source_folder, dependencies_extractor)

	save_jsons(project_folder, selected, dependencies, changed, new_hashes)

	if output: print_results(selected, output)

	if verbose: log(selected, dependencies, changed, test_files, source_files)

def parse_args():
	parser = arg_par(prog= 'python -m derts', description='Derts performs regression test selection. Given a codebase that has changed, it selects which tests should be executed. Find out more at https://github.com/GabrieleMaurina/derts')
	parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')
	parser.add_argument('-l', metavar='<lang profile>', default='c', help='set language profile (default "c")')
	parser.add_argument('-p', metavar='<project folder>', default='.', help='set project folder (default "current working directory")')
	parser.add_argument('-t', metavar='<test folder>', default='', help='set test folder relative to <project folder> (default same as <project folder>)')
	parser.add_argument('-s', metavar='<source folder>', default='', help='set source folder relative to <project folder> (default same as <project folder>)')
	parser.add_argument('-o', metavar='<output>', help='set output file (default no output, set to "stdout" for console output)')
	parser.add_argument('-d', metavar='<dep extractor>', help='set extractor file (default is internal, may not work on all systems)')
	args = parser.parse_args()
	if args.l == 'javascript': args.l = 'js'
	return args

def main():	
	args = parse_args()
	run(args.l, args.p, args.t, args.s, args.verbose, args.o, args.d)

if __name__ == '__main__':
	main()
