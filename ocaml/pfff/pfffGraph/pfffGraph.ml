open Printf

let lang = Sys.argv.(1)
let root = Sys.argv.(2)
let files = Find_source.files_of_root ~lang root
let _ = List.iter (fun s -> print_endline s) files

let verbose = true
let graph = match lang with
	| "ml"  -> Graph_code_ml.build ~verbose root files
	| "lisp" -> Graph_code_lisp.build ~verbose root files
	| "c" -> Graph_code_c.build ~verbose root files
	| "java" -> Graph_code_java.build ~verbose root files
	| "php" -> let g, _ = Graph_code_php.build ~verbose root files in g
	| "js" -> Graph_code_js.build ~verbose root files
	| _ -> failwith "Unsupported language."

let printNode graph (id, kind) = printf "%s %s %s\n" id (Entity_code.string_of_entity_kind kind) (try Graph_code.file_of_node (id, kind) graph with _ -> "$$$$$$$$$$$$$$$$$")

let _ = Graph_code.iter_nodes (printNode graph) graph
