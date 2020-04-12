#!/bin/bash

erlc server.erl utils.erl
erl -sname $1 -setcookie $2 -noshell -s server start
