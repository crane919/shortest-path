import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph, shortest_path):
    """
    Visualizes a given graph and highlights the shortest path between two nodes.

    This function takes a graph and a pre-calculated shortest path, and creates a visual 
    representation of the graph using NetworkX and Matplotlib. The nodes and edges of the 
    graph are plotted, with the edges labeled with their weights. The shortest path is 
    highlighted in the visualization.

    Parameters:
    graph (dict of tuple to float): A dictionary representing the graph. Keys are tuples 
                                    representing edges (node1, node2), and values are 
                                    the weights of these edges.
    shortest_path (list): A list of nodes representing the shortest path in the graph.

    Returns:
    None: The function does not return a value but displays a plot using Matplotlib.

    Note:
    - This function assumes that the input graph is undirected.
    - The shortest path is highlighted in blue and is displayed with a thicker line width.
    - Edge weights are rounded to two decimal places for clarity in the visualization.
    """

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

    # plot
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    nx.draw_networkx_labels(G,pos)
    nx.draw_networkx_edges(G, pos, shortest_path_edges, edge_color = 'b', width = 2)

    plt.show()
