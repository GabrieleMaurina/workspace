-module(lrs).
-export([lrs/2, slave/3]).

lrs(S, N) when N > 0 ->
	Size = string:len(S) div N,
	Rem = string:len(S) rem N,
	slaves(N, slice(S, Size, Rem)),
	wait(array:new(N), 0, N).

slice("", _, _) -> [];
slice(S, Size, Rem) when Rem > 0 -> [string:slice(S, 0, Size+1)|slice(string:slice(S, Size+1), Size, Rem-1)];
slice(S, Size, 0) -> [string:slice(S, 0, Size)|slice(string:slice(S, Size), Size, 0)].

slaves(0, _) -> ok;
slaves(N, []) -> spawn(lrs, slave, [N, "", self()]), slaves(N-1, []);
slaves(N, [S|T]) -> spawn(lrs, slave, [N, S, self()]), slaves(N-1, T).

slave(N, S, Master) ->
	io:format("Slave ~p, with pid ~p, reversed ~p into ~p\n", [N, self(), S, string:reverse(S)]),
	Master ! {N, string:reverse(S)}, exit(finished).

wait(Chunks, N, N) -> string:join(array:to_list(Chunks), "");
wait(Chunks, C, N) -> receive {I, S} -> wait(array:set(I-1, S, Chunks), C+1, N) end.
