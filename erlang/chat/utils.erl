-module(utils).
-export([name/1]).

name(Name) -> lists:nth(1, string:split(atom_to_list(Name), "@")).
