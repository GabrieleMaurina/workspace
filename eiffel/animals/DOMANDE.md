Dopo aver letto attentamente il codice fornito, rispondere alle seguenti
domande. (Il codice delle risposte può essere scritto qui o nei file Eiffel)


1. Si consideri l'assegnamento `f := g` nella feature `make` di `APPLICATION`:
   indicare l'effetto (ossia spiegare con precisione cosa succede volendo
   eseguire il programma, eventualmente indicando errori, specificandone se
   avvengono durante la compilazione o l'esecuzione) di un'istruzione
   `c.eat(f)`. Indicare l'effetto dell'istruzione `a.eat(f)` nel caso in cui
   fosse preceduta da un assegnamento `f := c`.

2. Indicare l'effetto dell'istruzione `a.eat(f)` nel caso in cui fosse preceduta
   da un assegnamento `f := a`.
   
3. Suggerire invarianti ragionevoli per la classe `GRASS` e pre- e
   post-condizioni per le feature `grow` e `consume`.

4. Proporre una precondizione ragionevole per la feature `eat` della classe
   `COW` e spiegare perché però non sarebbe efficace.
   
5. Riscrivere la feature `eat` della classe `COW` in modo che sollevi
   un'eccezione nel caso descritto alla domanda precedente. È una buona idea?
   Quale altra modalità sarebbe più conforme alla filosofia Design By Contract?
