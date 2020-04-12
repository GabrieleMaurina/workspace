note
	description: "Summary description for {COW}."
	author: ""
	date: "$Date$"
	revision: "$Revision$"

class
	COW

inherit

	ANIMAL
		redefine
			out
		end

feature

	eat (g: GRASS)
		local
		do
			g.consume (10)
		end

	out: STRING
		do
			Result := "a cow"
		end

end
