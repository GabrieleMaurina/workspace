note
	description: "Summary description for {ANIMAL}."
	author: ""
	date: "$Date$"
	revision: "$Revision$"

deferred class
	ANIMAL

inherit

	FOOD

feature

	eat (f: FOOD)
		require
			no_autophagy: f /= ({FOOD} [Current])
		deferred
		end

end
