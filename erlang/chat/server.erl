-module(server).
-import(utils, [name/1]).
-export([start/0, loop/1]).

start() ->
	io:format("Server name: ~s~nServer password: ~s~n",[name(node()), erlang:get_cookie()]),
	register(ser, spawn(server, loop, [sets:new()])),
	loop().

loop(Clients) ->
	receive
		{msg, Node, Msg} -> broadcast(Clients, Node, Msg), loop(Clients);
		{reg, Node} ->
			broadcast(Clients, io_lib:format("~s joined the chat.", [name(Node)])),
			loop(sets:add_element(Node, Clients));
		{unreg, Node} -> broadcast(Clients, io_lib:format("~s left the chat.", [name(Node)])), loop(sets:del_element(Node, Clients))
	end.

loop() ->
	ser ! {msg, node(), string:chomp(io:get_line(""))},
	loop().

broadcast(Clients, Node, Msg) ->
	Str = io_lib:format("~s:~s", [name(Node), Msg]),
	broadcast(Clients, Str).

broadcast(Clients, Msg) ->
	io:format("~s~n",[Msg]),
	lists:foreach(fun(Cli) -> {cli,Cli} ! Msg end, sets:to_list(Clients)).
