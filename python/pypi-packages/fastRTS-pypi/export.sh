#!/usr/bin/env bash

mkdir fastRTS
#cp ~/workspace/fastRTS/fastRTS.py fastRTS/
#cp ~/workspace/fastRTS/README.md fastRTS/
cp setup.py fastRTS/

cd fastRTS
	echo 'import dext' > fastrts.py
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf fastRTS
