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
let dependencies = Hashtbl.create 1000
let get_node_file (id, kind) = try Graph_code.file_of_node (id, kind) graph with _ -> ""
let store_edge node1 node2 = match (get_node_file node1), (get_node_file node2) with
	| "",_ -> ()
	| _,"" -> ()
	| file1, file2 -> if file1 <> file2 then Hashtbl.replace dependencies (file1, file2) ()
let _ = Graph_code.iter_use_edges store_edge graph
let print_dependency (file1, file2) _ = Printf.printf "%s %s\n" file1 file2
let _ = Hashtbl.iter print_dependency dependencies
