#!/usr/bin/env bash

cp -r ~/Documents/workspace/git/fastrts ./
cp setup.py fastrts/

cd fastrts
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
	#python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
cd ..

rm -rf fastrts
