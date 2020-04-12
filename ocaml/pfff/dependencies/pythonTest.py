#!/usr/bin/env python3

from os.path import relpath
import subprocess

def get_dependencies(language, project_folder):
	result = subprocess.run(
		args=['./dependencies.exe', language, project_folder],
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

print(get_dependencies('c', '/home/gabriele/Documents/workspace/git/codegraph/tests/c/'))
