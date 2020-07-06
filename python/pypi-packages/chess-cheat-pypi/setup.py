import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='chess-cheat',
	version='1.0.3',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='Chess-Cheat is a tool to cheat at online chess',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/chess-cheat',
	py_modules=['chess-cheat'],
	packages=['chess_cheat_utils'],
	include_package_data=True,
	licence='MIT',
	install_requires=['tensorflow', 'stockfish', 'pillow', 'pyscreenshot', 'timeout-decorator', 'numpy'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
