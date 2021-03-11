#!/usr/bin/env bash

mkdir ram
cp ~/workspace/random-access-machine/ram.py ram/
cp ~/workspace/random-access-machine/README.md ram/
cp setup.py ram/

cd ram
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf ram
