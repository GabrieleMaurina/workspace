-module(sequential).
-export([is_palindrome/1, is_an_anagram/2, factors/1, is_proper/1]).

is_palindrome(S) -> S == string:reverse(S).

is_an_anagram(_, []) -> false;
is_an_anagram(S, [H|T]) ->
				A = anagram(S,H),
				if
					A -> true;
					true -> is_an_anagram(S, T)
				end.
anagram("", "") -> true;
anagram(S1, S2) ->
			L1 = string:len(S1),
			L2 = string:len(S2),
			if
				L1 /= L2 -> false;
				true -> anagram(string:slice(S1, 1), unicode:characters_to_list(string:replace(S2, string:slice(S1, 0, 1), "")))
			end.

factors(0) -> [];
factors(1) -> [1];
factors(N) when N < 0 -> factors(-N);
factors(N) -> [1|lists:reverse(factors(N, 2, []))].

factors(N, D, L) when D >= N -> [N|L];
factors(N, D, L) when N rem D == 0 -> factors(N, D+1, [D|L]);
factors(N, D, L) -> factors(N, D+1, L).

is_proper(N) -> lists:sum(factors(N)) == N + N.
