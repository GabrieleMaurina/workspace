#!/usr/bin/env bash

cp -r ~/workspace/dext ./
cp setup.py dext/

cd dext
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf dext
