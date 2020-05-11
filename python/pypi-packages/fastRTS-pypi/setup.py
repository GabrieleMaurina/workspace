import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='fastrts',
	version='1.0.6',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='FastRTS is a tool to perform regression test selection.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/fastRTS',
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