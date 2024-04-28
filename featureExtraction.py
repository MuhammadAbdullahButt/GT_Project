import networkx as nx
import pandas as pd
import numpy as np
from pysubgroup import SubgroupDiscoveryTask, create_nominal_selectors

def frequent_subgraph_mining(training_graphs):
    # Convert NetworkX graphs to pandas DataFrame-like format
    graph_data = [{'graph': nx.to_pandas_adjacency(graph)} for graph in training_graphs]

    # Concatenate adjacency matrices into a single DataFrame
    all_graphs_df = pd.concat([pd.DataFrame(graph['graph']) for graph in graph_data], axis=0)
    
    print(type(all_graphs_df))  # Add this line to check the type of all_graphs_df

    # Define the search space using nominal selectors
    nominal_selectors = create_nominal_selectors(all_graphs_df.columns.tolist())
    
    # Define the search space as a conjunction of selectors
    search_space = [selector for selector in nominal_selectors]
    
    # Define the subgroup discovery task with search space and quality function
    task = SubgroupDiscoveryTask(graph_data, target='graph', depth=3, search_space=search_space)
    
    # Run frequent subgraph mining algorithm
    result = task.find_subgroups()
    
    return result


def extract_features(training_graphs, frequent_subgraphs):
    # Extract features from training graphs based on frequent subgraphs
    feature_matrix = []
    for graph in training_graphs:
        features = []
        for subgraph in frequent_subgraphs:
            if nx.is_subgraph(graph, subgraph):
                features.append(1)
            else:
                features.append(0)
        feature_matrix.append(features)
    
    return np.array(feature_matrix)
