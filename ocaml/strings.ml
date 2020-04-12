module Strings:
sig
	val is_palindrome : string -> bool
	val (-) : string -> string -> string
	val anagram : string -> string list -> bool
end=
struct
	let reverse s = 
		let l = String.length s - 1
		in String.mapi (fun i c -> s.[l-i]) s

	let is_palindrome s = (String.lowercase_ascii s) = reverse(String.lowercase_ascii s)

	let filter f s =
		let l = String.length s
		in let rec build i w = if i >= l then w else build (i+1) (if f s.[i] then w ^ (String.make 1 s.[i]) else w)
		in build 0 ""

	let (-) s1 s2 = filter (fun c -> not (String.contains s2 c)) s1

	let remove s c =
		let rec loop s i c = if i < 0 then s else if s.[i] = c then ((String.sub s 0 i) ^ (String.sub s (i+1) (Pervasives.(-) (Pervasives.(-) (String.length s) i) 1))) else loop s (Pervasives.(-) i 1) c
		in loop s (Pervasives.(-) (String.length s) 1) c

	let rec anagrams s1 s2 = match (s1, s2) with
		("", "") -> true
		| (s1, s2) -> if String.length s1 <> String.length s2 then false else anagrams (remove s1 s1.[0]) (remove s2 s1.[0])

	let rec anagram s = function
		[] -> false
		| h::t -> if anagrams s h then true else anagram s t
end
