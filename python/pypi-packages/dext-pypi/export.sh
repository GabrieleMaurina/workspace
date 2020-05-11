#!/usr/bin/env bash

mkdir dext
cp ~/workspace/dext/dext.py dext/
cp ~/workspace/dext/README.md dext/
cp setup.py dext/

cd dext
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf dext
