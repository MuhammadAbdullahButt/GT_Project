import networkx as nx
import matplotlib.pyplot as plt
from graphPlotting import create_graph_from_file
# Your existing code for computing similarity and KNN classification

def visualize_graph(graph, title):
    plt.figure(figsize=(8, 6))
    plt.title(title)
    pos = nx.spring_layout(graph)  # Position nodes using the spring layout algorithm
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    plt.show()

def compute_similarity(graph1, graph2):
    # Find the isomorphism between graph1 and graph2
    matcher = nx.algorithms.isomorphism.GraphMatcher(graph1, graph2)
    # Get the mapping between nodes in graph1 and graph2
    isomorphism = matcher.isomorphisms_iter()
    
    # Check if any isomorphisms were found
    try:
        mcs_nodes = max(isomorphism, key=len)
    except ValueError:
        # If no isomorphisms found, similarity is zero
        return 0.0
    
    # Extract the largest common subgraph from the isomorphism
    mcs = graph1.subgraph(mcs_nodes)
    
    # Check if either graph has no edges
    if len(graph1.edges) == 0 or len(graph2.edges) == 0:
        return 0.0  # Return zero similarity if either graph has no edges
    
    # Calculate the similarity based on the size of the MCS
    similarity = len(mcs.edges) / min(len(graph1.edges), len(graph2.edges))
    
    return similarity

def knn_classify(test_graph, training_graphs, labels, k):
    distances = []
    for i, train_graph in enumerate(training_graphs):
        similarity = compute_similarity(test_graph, train_graph)
        distances.append((similarity, labels[i]))  # Store similarity and corresponding label
    # Sort the distances based on similarity in descending order
    distances.sort(reverse=True)
    # Select the k-nearest neighbors
    nearest_neighbors = distances[:k]
    # Count the occurrences of each class among the nearest neighbors
    class_counts = {}
    for _, label in nearest_neighbors:
        class_counts[label] = class_counts.get(label, 0) + 1
    # Determine the majority class
    majority_class = max(class_counts, key=class_counts.get)
    return majority_class

def load_graph_from_file(file_path):
    # Initialize an empty graph
    graph = nx.Graph()

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        # Assuming each line represents an edge in the format "node1 node2"
        for line in file:
            # Split the line into node1 and node2
            nodes = line.strip().split()
            if len(nodes) == 2:  # Ensure the line contains two nodes
                node1, node2 = nodes
                # Add the edge to the graph
                graph.add_edge(node1, node2)

    return graph
# Example usage:
test_graphs = [
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_test_1.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_test_2.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_test_3.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_test_1.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_test_2.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_test_3.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_test_1.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_test_2.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_test_3.txt"),
]

test_graphs2 = [
    "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_test_1.txt",
    "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_test_2.txt",
    "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_test_3.txt",
    "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_test_1.txt",
    "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_test_2.txt",
    "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_test_3.txt",
    "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_test_1.txt",
    "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_test_2.txt",
    "C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_test_3.txt",
]

training_graphs = [
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_1.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_2.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_3.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_4.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_5.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_6.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_7.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_8.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_9.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_10.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_11.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sports/p_sports_train_12.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_1.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_2.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_3.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_4.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_5.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_6.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_7.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_8.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_9.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_10.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_11.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/sci&edu/p_sci&edu_train_12.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_1.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_2.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_3.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_4.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_5.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_6.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_7.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_8.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_9.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_10.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_11.txt"),
    load_graph_from_file("C:/Users/abdul/Desktop/PROGRAMMING/GT/preprocessedFiles/dis&symp/p_dis&symp_train_12.txt"),
]

labels = ["Science&education", "Sports", "Disease&Symptoms"] * (len(training_graphs) // 3)

k = 5

predicted_classes = []
for test_graph in test_graphs:
    predicted_class = knn_classify(test_graph, training_graphs, labels, k)
    predicted_classes.append(predicted_class)

print("Predicted classes:", predicted_classes)

# Visualize test graphs
for i, test_graph in enumerate(test_graphs2):
    graph = create_graph_from_file(test_graph)
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

# Visualize training graphs
#for i, train_graph in enumerate(training_graphs):
#    visualize_graph(train_graph, f"Training Graph {i+1}")
