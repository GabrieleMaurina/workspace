import setuptools

#with open('README.md', 'r') as fh:
#	long_description = fh.read()

setuptools.setup(
	name='derts',
	version='0.0.1',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='Derts is a tool to perform regression test selection.',
	#long_description=long_description,
	#long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/fastRTS',
	licence='MIT',
	py_modules=['derts'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
