import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='while-machine',
	version='1.0.1',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='While Abstract Machine implemented in python.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/while-machine',
	licence='MIT',
	py_modules=['while_machine'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
