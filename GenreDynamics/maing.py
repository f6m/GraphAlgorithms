#https://www.geeksforgeeks.org/python/different-ways-to-create-pandas-dataframe/
#https://www.geeksforgeeks.org/python/pandas-dataframe-to_dict/
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
k = 5
N = 2*k #Order of the graph
m = [0] * k
h = [1] * k
genre = h + m #Vertex label partition
vert = range(1,N+1)
np.random.shuffle(genre)
print(vert)
b = [np.random.uniform(0,1) for _ in range(N)]
print(b)

#Dataframe
data =pd.DataFrame({'vertex': vert, 'genero': genre, 'body': b})
#data1 = {'vertex': [1, 2, 3, 4],
 #       'body': [0.2, 0.5, 0.2, 0.5]}
#dat = pd.DataFrame(data)
print(data)

#dt = pd.DataFrame(data)
#dt.drop_duplicates(inplace=True)
#print(dt)

#Dataframe -> Graph
G = nx.Graph() # Create an empty undirected graph 
G.add_nodes_from(data['vertex']) # Asociate nodes based on Dataframe vertex
vertex_attrib=data.set_index('vertex').to_dict(orient='index') # Dicctionary data structure
nx.set_node_attributes(G, vertex_attrib)

print(G.nodes[1])

#Sampling

#Select a node randomly, which distribution?
# Select nodes where 'type' is 'city'
hombres = []
for node, attributes in G.nodes(data=True):
    if attributes.get("genero") == 1:
        hombres.append(node)

u = np.random.choice(hombres)
v = np.random.choice(list(G.nodes()))

if not G.has_edge(u,v) and u != v:
    G.add_edge(u,v)

print('Vertices elegidos:',u,v)
#print(n1)
#nodes = list(G.nodes())
#n1, n2 = random.sample(nodes,2)

#W U M = V

#if not G.has_edge(n1,n2) and n1 != n2:
#  G.add_edge(n1,n2)

# Add nodes from the 'source' and 'target' columns
#G.add_nodes_from(df['source'])
#G.add_nodes_from(df['target'])
# Add edges from the DataFrame
#edges = [(row['source'], row['target']) for index, row in df.iterrows()]
#print(edges)
#G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G) # Define the layout for node positioning
nx.draw(G, pos, with_labels=True, node_size=100, node_color='skyblue', font_size=10, font_color='black')
# Display the graph
plt.show()
