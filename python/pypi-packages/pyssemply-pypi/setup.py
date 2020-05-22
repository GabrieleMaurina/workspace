import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='pyssembly',
	version='1.0.5',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='Pyssembly allows to execute pseudo assembly code and it is meant for teaching purposes.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/pyssembly',
	licence='MIT',
	py_modules=['pyssembly'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
