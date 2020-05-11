#!/usr/bin/env bash

mkdir fastTP
#cp ~/workspace/fastTP/fastTP.py fastTP/
#cp ~/workspace/fastTP/README.ml fastTP/
echo 'import dext' > fastTP/fasttp.py
cp setup.py fastTP/

cd fastTP
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf fastTP
