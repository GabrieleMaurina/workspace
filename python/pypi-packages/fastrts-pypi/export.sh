#!/usr/bin/env bash

cp -r ~/workspace/fastrts ./
cp setup.py fastrts/

cd fastrts
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf fastrts
