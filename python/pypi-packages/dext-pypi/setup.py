import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='dext',
	version='1.0.3',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='Dext is a tool to extract file dependencies from a code base.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/dext',
	licence='MIT',
	py_modules=['dext'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
