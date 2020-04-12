let an = [4;12;20;38;56;88];;
let ng = [2;10;18;36;54;86];;
let ngn = ["helium";"neon";"argon";"krypton";"xenon";"radon"]
let rec max x = function
	[] -> x
	| h::t -> if h > max x t then h else max x t;;
let rec zip l1 l2 =
	match (l1, l2) with
	([],[]) | ([],_) | (_,[]) -> []
	| (h1::t1,h2::t2) -> (h1, h2)::(zip t1 t2);;
let rec sort c = function
	[] -> []
	| h::t -> ((sort c (List.filter (fun e -> c h e) t)) @ [h] @ (sort c (List.filter(fun e -> c e h) t )));;
let rec rev = function
	[] -> []
	| h::t -> rev t @ [h];;
print_endline(string_of_int(max 0 an));;
