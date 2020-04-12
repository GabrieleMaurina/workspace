let verbose = false
let lang = Sys.argv.(1)
let root = Sys.argv.(2)
let files = Find_source.files_of_root ~lang root
let graph = match lang with
	| "ml"  -> Graph_code_ml.build ~verbose root files
	| "lisp" -> Graph_code_lisp.build ~verbose root files
	| "c" -> Graph_code_c.build ~verbose root files
	| "java" -> Graph_code_java.build ~verbose root files
	| "php" -> let g, _ = Graph_code_php.build ~verbose root files in g
	| "js" -> Graph_code_js.build ~verbose root files
	| _ -> failwith "Unsupported language."

let node_json (id, kind) = Printf.sprintf "[\"%s\",\"%s\",\"%s\"]" id (Entity_code.string_of_entity_kind kind) (try Graph_code.file_of_node (id, kind) graph with _ -> "")
let edge_json node1 node2 = Printf.printf "[%s,%s],\n" (node_json node1) (node_json node2)

let _ = Graph_code.iter_use_edges edge_json graph
