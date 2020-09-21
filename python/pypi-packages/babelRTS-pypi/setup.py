import setuptools
import babelrts

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='babelrts',
	version=babelrts.__version__,
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='BastRTS is a tool to perform regression test selection.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/babelRTS',
	licence='MIT',
	py_modules=['babelrts'],
	install_requires=['dext'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
