import os
import networkx as nx
from graphPlotting import create_graph_from_file  # Import your function for generating graphs from text
from pysubgroup.search import search


def load_graphs_from_folder(folder_path):
    graphs = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Generate graph from text data
        G = create_graph_from_file(file_path)  # Pass file path instead of text_data
        graphs.append(G)
    return graphs

# Step 2: Frequent Subgraph Mining
def frequent_subgraph_mining(graphs, min_support):
    frequent_subgraphs = search(graphs, min_support=min_support, verbosity=2)
    return frequent_subgraphs

# Load preprocessed graphs
preprocessed_folder = 'C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp'
graphs = load_graphs_from_folder(preprocessed_folder)

#Example usage:
min_support = 0.5  # Adjust the minimum support threshold
frequent_subgraphs = frequent_subgraph_mining(graphs, min_support)

# Print the frequent subgraphs
for sg in frequent_subgraphs:
    print(sg)



# Step 3: Feature Extraction
# Implement feature extraction from identified frequent subgraphs
# You might want to represent each graph/document as a feature vector
# where each element corresponds to the presence or count of a frequent subgraph


