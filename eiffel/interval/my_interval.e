note
	description: "Esame di Sviluppo software in gruppi di lavoro complessi"
	author: "Mattia Monga"

deferred class
	MY_INTERVAL

feature

	make (l, u: INTEGER)
			-- Set bounds to l and u;make interval empty if l > u.
		deferred
		ensure
			lower_set: lower = l
			upper_set: upper = u
			bounds_l_must_be_less_or_equal_to_u: l <= u
		end

feature -- Access

	lower: INTEGER

	upper: INTEGER

feature -- Comparison

	is_comparable (other: like Current): BOOLEAN
			-- Is either one of current interval and other
			-- strictly contained in the other?
		deferred
		ensure
			definition: Result = (Current < other) or ((Current ~ other)) or (Current > other)
		end

	is_subinterval alias "<" (other: like Current): BOOLEAN
			-- Is current interval strictly included in other?
		deferred
		ensure
			definition: lower > other.lower and upper < other.upper
		end

	is_superinterval alias ">" (other: like Current): BOOLEAN
			-- Does current interval strictly include other?
		deferred
		ensure
			definition: other < Current
		end

	extend_to (i: INTEGER)
		-- Non ci sono precondizioni. Se i è già nell'intervallo, nulla accade.
		-- Se i ha un valore maggiore di upper, upper viene esteso per includere i.
		-- Se i ha un valore minore di lower, lower viene abbassato per includere i.
		-- Nel caso in cui lower > upper, cioè l'intervallo è vuoto, è possibile che
		-- sia lower che upper vengano modificati. Questo accade by design.
		do
			if i < lower
			then lower := i
			end
			if i > upper
			then upper := i
			end
		ensure
			extended_correctly: i <= upper and i >= lower
		end

feature -- Status report

	is_empty: BOOLEAN
			-- Does interval contain no values?
		do
			Result := lower > upper
		end
	-- La feature is_empty non ha nessuna post condizione poichè non modifica lo stato dell'oggetto,
	-- quindi non ci sono valori da controllare. Inoltre la sua correttezza è già verificata dall'invariante empty_if_no_values.
	-- Inoltre una post condizione del tipo:
	-- ensure
	--	correct: Result = lower > upper
	-- end
	-- risulterebbe quasi superflua perchè praticamente identica al codice stesso della feature.
	-- In sostanza avere una post condizione sarebbe ridondante.

invariant
	empty_if_no_values: is_empty = (lower > upper)

end
