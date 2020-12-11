#!/usr/bin/env bash

mkdir dext
cd dext

	cp ../setup_empty.py .
	touch dext.py
	python -m pip install --upgrade twine setuptools wheel --user
	python setup_empty.py sdist bdist_wheel
	python -m twine upload dist/*

cd ..
rm -rf dext
