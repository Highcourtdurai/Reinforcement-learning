from networkx import nx
import matplotlib.pyplot as plt
import numpy as np

MATRIX_SIZE=11
M=np.matrix(np.ones(shape=(MATRIX_SIZE,MATRIX_SIZE)))
M*=-1
edges=[(0,1),(1,5),(5,6),(5,4),(1,2),
       (1,3),(9,10),(2,4),(0,6),(6,7),
       (8,9),(7,8),(1,7),(3,9)]

g=nx.Graph()
g.add_edges_from(edges)
pos=nx.spring_layout(g)
nx.draw_networkx_nodes(g,pos)
nx.draw_networkx_edges(g,pos)
nx.draw_networkx_labels(g,pos)
plt.show()
goal=10
for point in edges:
    print(point)
    if point[1] == goal:
        M[point]=1000
    else:
        M[point]=0
        
    if point[0] ==goal:
        M[point[::-1]]=100
    else:
        M[point[::-1]] =0
        #reverse of point
    
M[goal, goal] =100

        