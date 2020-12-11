import setuptools

setuptools.setup(
	name='dext',
	version='1.1.10',
	author='Gabriele Maurina',
	author_email='gabrielemaurina95@gmail.com',
	description='Dext is a tool to extract file dependencies from a code base. It is still under development.',
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
