#!/usr/bin/env bash

mkdir babelRTS
cd babelRTS

	cp ../setup_empty.py .
	touch babelrts.py
	python -m pip install --upgrade twine setuptools wheel --user
	python setup_empty.py sdist bdist_wheel
	python -m twine upload dist/*

cd ..
rm -rf babelRTS
