#!/usr/bin/env bash

mkdir dext

cd dext
	cp ~/workspace/dext/dext.py .
	cp ~/workspace/dext/README.md .
	cp ../setup.py .
	
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf dext
