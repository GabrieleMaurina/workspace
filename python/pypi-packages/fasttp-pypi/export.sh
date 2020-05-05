#!/usr/bin/env bash

#cp -r ~/workspace/fasttp ./
mkdir fasttp
echo 'import dext' > fasttp/fasttp.py
cp setup.py fasttp/

cd fasttp
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf fasttp
