#!/usr/bin/env bash

mkdir derts
cp setup.py derts/
#cp -r ~workspace/git/derts/* ./derts
echo "from sys import argv" > derts/derts.py

cd derts
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
	#python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
cd ..

rm -rf derts
