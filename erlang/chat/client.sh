#!/bin/bash

erlc client.erl utils.erl
erl -sname $3 -setcookie $2 -noshell -s client start $1
