-module(test).
-export([test/0, guard_test/2, true/0, false/0, loop/0]).

test() -> io:format("Hello Erlang\n", []).

guard_test(X, Y) when X > 2 -> io:format("X > 2\n", []);
guard_test(X, Y) when X == 1; Y > 3 -> io:format("X == 1 and Y > 3\n", []);
guard_test(X, Y) -> io:format("everything else\n", []).

true() -> io:format("True function\n", []), true.
false() -> io:format("False function\n", []), false.

loop() -> receive Any -> io:format("~p received ~p\n", [self(), Any]) end, loop().
