import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='random-access-machine',
	version='1.0.0',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='Random Access Machine implemented in python.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/random-access-machine',
	licence='MIT',
	py_modules=['ram'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
