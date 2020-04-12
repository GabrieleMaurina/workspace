#!/usr/bin/env bash

rm -f dependencies.exe
dune build dependencies.exe
mv _build/default/dependencies.exe ./
rm -rf _build .merlin
rm -f dune-project
