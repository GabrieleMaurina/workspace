#!/usr/bin/env bash

mkdir pyssembly
cp ~/workspace/pyssembly/pyssembly.py pyssembly/
cp ~/workspace/pyssembly/README.md pyssembly/
cp setup.py pyssembly/

cd pyssembly
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf pyssembly
