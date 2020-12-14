from graphviz import Digraph as G

g = G("asdf", filename=str(1) + 'svg', format='svg')
g.edge('A', 'B')
g.view()
