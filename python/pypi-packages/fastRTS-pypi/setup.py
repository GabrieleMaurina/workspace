import setuptools

#with open('README.md', 'r') as fh:
#	long_description = fh.read()

setuptools.setup(
	name='fastrts',
	version='1.0.7',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='FastRTS has been renamed BabelRTS. Check it out here: https://github.com/GabrieleMaurina/babelRTS. Install it with "python -m pip install babelrts".',
	long_description='FastRTS has been renamed BabelRTS. Check it out here: https://github.com/GabrieleMaurina/babelRTS. Install it with "python -m pip install babelrts".',
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/babelRTS',
	licence='MIT',
	py_modules=['fastrts'],
	install_requires=['dext'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
