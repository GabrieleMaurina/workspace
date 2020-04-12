-module(server).
-export([start/0, loop/0]).

start() -> register(ser, spawn(server,loop,[])).

loop() -> receive
		{Pid, Node, Msg} ->
			io:format("~p   ###   ~p   ###   ~p~n", [Pid, Node, Msg]),
			{Pid, Node} ! {self(), node(), "Hello from server."}
	end, loop().
