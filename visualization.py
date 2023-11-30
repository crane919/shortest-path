import matplotlib.pyplot as plt
import random
import networkx as nx
import json

# def addEdge(edge_list, vertex_1, vertex_2):
#     edge_list[vertex_1].append(vertex_2)  # adds vertex_2 to vertex_1s adjacencies
#     edge_list[vertex_2].append(vertex_1)  # adds vertex_1 to vertex_2s adjacencies

#     return edge_list  # returns the entire edge list

# def generate_random_graph(num_vertices, num_edges):
#     # Maximum possible edges for v vertices
#     max_edges = num_vertices * (num_vertices - 1) // 2

#     if num_edges > max_edges:
#         raise ValueError(
#             f"Cannot form {num_edges} edges with only {num_vertices} vertices. Maximum possible edges are {max_edges}."
#         )

#     edge_list = [[] for _ in range(num_vertices)]
#     num_edges_in_list = 0

#     while num_edges_in_list < num_edges:
#         vertex1 = random.randint(0, num_vertices - 1)
#         vertex2 = random.randint(0, num_vertices - 1)

#         # Ensure no self-loops and no duplicate edges
#         if (
#             vertex1 != vertex2
#             and vertex1 not in edge_list[vertex2]
#             and vertex2 not in edge_list[vertex1]
#         ):
#             addEdge(edge_list, vertex1, vertex2)
#             num_edges_in_list += 1

#     return edge_list


def visualize_graph(graph, shortest_path):
    # convert to graph
    G = nx.Graph()
    shortest_path_edges = []
    for n in range(len(shortest_path)-1):
        shortest_path_edges.append((shortest_path[n], shortest_path[n+1]))

    for (node1,node2), weight in graph.items():
        G.add_edge(node1, node2, weight=weight)
    # compute layout for plotting
    pos = nx.kamada_kawai_layout(G, weight='weight')
    nx.draw(G,pos)
    labels = {k: round(v,2) for k,v in nx.get_edge_attributes(G,'weight').items()}
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edges(G, pos, shortest_path_edges, edge_color = 'b', width = 2)



    plt.show()


# routes = [[2, 1, 4, 3, 11], [1, 0, 3, 11, 10], [10, 11, 3, 4, 1]]
# edges = []
# for r in routes:
#     route_edges = [(r[n],r[n+1]) for n in range(len(r)-1)]
#     G.add_nodes_from(r)
#     G.add_edges_from(route_edges)
#     edges.append(route_edges)

# print("Graph has %d nodes with %d edges" %(G.number_of_nodes(),    
# G.number_of_edges()))

# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G,pos=pos)
# nx.draw_networkx_labels(G,pos=pos)
# colors = ['r', 'b', 'y']
# linewidths = [20,10,5]
# for ctr, edgelist in enumerate(edges):
#     nx.draw_networkx_edges(G,pos=pos,edgelist=edgelist,edge_color = colors[ctr], width=linewidths[ctr])
# plt.savefig('this.png')


# def save_graph_data(
# graph
# ):
#     graph_data = {
#         "edge_list": edge_list,
#         "coloring_1_name": coloring_1_name,
#         "colors_1": colors_1,
#         "coloring_2_name": coloring_2_name,
#         "colors_2": colors_2,
#         "coloring_3_name": coloring_3_name,
#         "colors_3": colors_3,
#     }

#     filename = "graph_data.json"

#     try:
#         # Load existing data if the file already exists
#         with open(filename, "r") as f:
#             data = json.load(f)
#         data.append(graph_data)
#     except FileNotFoundError:
#         # If the file doesn't exist, create a new list
#         data = [graph_data]

#     # Save the updated data
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)
