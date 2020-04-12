-module(client).
-import(utils,[name/1]).
-export([start/1, loop/0]).

start([Server]) ->
	try
	io:format("Server name: ~s~nServer password: ~s~nClient name: ~s~n",[name(Server), erlang:get_cookie(), name(node())]),
	register(cli, spawn(client, loop, [])),
	reg(Server),
	loop(Server)
	of _ -> ok
	catch _ -> io:format("bye",[])
	end.

loop() -> receive Msg -> io:format("~s~n", [Msg]), loop() end.

loop(Server) ->
	{ser, Server} ! {msg, node(), string:chomp(io:get_line(""))},
	loop(Server).

reg(Server) -> {ser, Server} ! {reg, node()}.

unreg(Server) -> {ser, Server} ! {unreg, node()}.
