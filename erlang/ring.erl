-module(ring).
-export([start/3, next/2]).

start(M, N, MSG) ->
	PID = spawn(ring, next, [N, self()]),
	%sleep(1000),
	sendMsg(M, PID, MSG).

next(N, S) when N > 1 ->
	print(N),
	PID = spawn(ring, next, [N-1, S]),
	link(PID),
	getMsg(N, PID);
next(N, S) when N > 0 ->
	print(N),
	getMsg(N,S).

getMsg(N, PID) ->
	receive
		{MSG} ->
			io:format("~p ~p message received: ~p\n", [self(), N, MSG]),
			PID ! {MSG},
			getMsg(N, PID)
	end.

sendMsg(M, PID, MSG) when M > 0 ->
	PID ! {MSG},
	receive {RES} -> io:format("~p message looped around the ring: ~p\n", [self(), RES]) end,
	sendMsg(M-1, PID, MSG);
sendMsg(_, _, _) -> void.

print(N) -> io:format("~p ~p created\n", [self(), N]).

sleep(T) -> receive after T -> void end.
