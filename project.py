import networkx
from sympy.logic.boolalg import to_dnf
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
import time
import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
# necessary inputs
node_num = int(input("Enter numbers of nodes: "))
edge_num = int(input("Enter numbers of edges: "))
tuple_temp = ()
edges = []
nodes = []
if node_num > 52:
    print("Enter label of nodes in your graph:")
    nodes = [input() for i in range(node_num)]
else:
    if node_num < 27:
        nodes = [lower[j] for j in range(node_num)]
    elif 26 < node_num < 53:
        nodes = lower + [upper[j] for j in range(node_num - 26)]
    print("label of nodes in your graph:\n", nodes)

for i in range(1, edge_num + 1):
    print("Enter end nodes of edge", i)
    tuple_temp = (input("node1:"), input("node2:"))
    edges.append(tuple_temp)

# generate graph
w = 12
h = 9
d = 100
plt.figure(figsize=(w, h), dpi=d)
G = networkx.Graph()
G.add_edges_from(edges)
G.add_nodes_from(nodes)

start_time = time.time()
# compute number of MISs

E = parse_expr(edges[0][0] + "|" + edges[0][1])
for i in range(1, len(edges)):
    E = E & (parse_expr(edges[i][0] + "|" + edges[i][1]))
E = to_dnf(E, simplify=True, force=True)
expr = (' ' + str(E) + ' ').split("|")
print("\nnumber of MISs in this graph: ", len(expr))

# find MISs
temp = ""
temp1 = []
MIS = []
for i in range(len(expr)):
    temp2 = [' ' + j + ' ' for j in nodes]
    temp = expr[i][1] if len(expr[i]) == 3 else expr[i][2:len(expr[i]) - 2]
    temp1 = (' ' + temp + ' ').split("&")
    temp2 = [item for item in temp2 if item not in temp1]
    temp1 = []
    MIS.append(temp2)
print("MISs in this graph: ")
for i in MIS:
    print(i)
print("\nAlgorithm time:", (time.time()) - start_time)

# plot graph
networkx.draw_networkx(G, with_labels=nodes)
plt.axis("off")
plt.show()
plt.savefig("out.png")
