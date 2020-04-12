module Calculator =
struct
	let eval s =
		let l = List.rev (String.split_on_char ' ' s)
		in let op = function
			"+" -> (+)
			| "-" -> (-)
			| "*" -> ( * )
			| "/" -> (/)
			| "**" -> fun a b -> let rec pow n e r = if e = 0 then r else pow n (e-1) (r*n)
						in pow a b 1
			| _ -> raise Not_found
		in let rec compute h = function
			[] -> 0
			| [c] -> int_of_string c
			| f::s::t::tail -> try
						let o1 = int_of_string s
						in let o2 = int_of_string f
						in let op = op t
						in compute [] ((List.rev h) @ [string_of_int (op o1 o2)] @ tail)
					with _ -> compute (f::h) (s::t::tail)
		in compute [] l
end
