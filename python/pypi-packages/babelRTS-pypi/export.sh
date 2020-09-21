#!/usr/bin/env bash

mkdir babelRTS

cd babelRTS
	cp ~/workspace/babelRTS/babelrts.py .
	cp ~/workspace/babelRTS/README.md .
	cp ../setup.py .

	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf babelRTS
