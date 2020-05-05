import setuptools

#with open('README.md', 'r') as fh:
#	long_description = fh.read()

setuptools.setup(
	name='fasttp',
	version='0.0.1',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='Fasttp is a tool to perform test case prioritization.',
#	long_description=long_description,
#	long_description_content_type='text/markdown',
	url='https://github.com/GabrieleMaurina/fasttp',
	licence='MIT',
	py_modules=['fasttp'],
	install_requires=['dext'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.8',
)
