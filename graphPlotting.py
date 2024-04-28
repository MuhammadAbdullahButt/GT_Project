import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

def create_graph_from_file(input_file_path, threshold=3):
    # Read preprocessed data from file
    with open(input_file_path, "r", encoding="utf-8") as file:
        preprocessed_data = [line.split() for line in file]

    # Call create_graph function with preprocessed data
    return create_graph(preprocessed_data, threshold)

def create_graph(preprocessed_data, threshold=2):
    # Initialize directed graph
    G = nx.DiGraph()
    
    # Count term occurrences
    term_counts = Counter()
    for document in preprocessed_data:
        term_counts.update(document)
    
    # Filter terms based on threshold
    filtered_terms = {term for term, count in term_counts.items() if count >= threshold}
    
    # Iterate through each document in the preprocessed data
    for document in preprocessed_data:
        # Generate all possible pairs of adjacent terms
        pairs = [(document[i], document[i+1]) for i in range(len(document)-1) if document[i] in filtered_terms and document[i+1] in filtered_terms]
        
        # Count the occurrences of each term pair
        pair_counts = Counter(pairs)
        
        # Add edges to the graph
        for pair, count in pair_counts.items():
            term1, term2 = pair
            G.add_edge(term1, term2, weight=count)
    
    return G


'''
# Example usage:
input_file_path = "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_1.txt"
threshold = 5  # Adjust the threshold as needed
graph = create_graph_from_file(input_file_path, threshold)

# Example usage: Calculate the number of nodes and edges in the graph
num_nodes = len(graph.nodes)
num_edges = len(graph.edges)

print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(graph, k=0.15, iterations=50, seed=42)  # Adjust layout parameters
nx.draw(graph, pos, with_labels=True, node_size=800, node_color='blue', edge_color='black', arrowsize=10, font_size=10)
plt.title("Directed Graph of Unique Terms")
plt.show()
'''