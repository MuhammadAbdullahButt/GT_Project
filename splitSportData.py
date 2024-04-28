import os
from sklearn.model_selection import train_test_split

# Define the path to the directory containing the preprocessed files
data_directory = "C:/Users/abdul/Desktop/PROGRAMMING/GT"

# Get the list of preprocessed files for training
train_files = [os.path.join(data_directory, filename) for filename in os.listdir(data_directory) if filename.startswith("p_sci&edu_train")]

# Get the list of preprocessed files for test
test_files = [os.path.join(data_directory, filename) for filename in os.listdir(data_directory) if filename.startswith("p_sci&edu_test")]

# Split the training data into train and validation sets
train_data = []
validation_data = []
for train_file in train_files:
    with open(train_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        # Check if the file contains enough samples
        if len(lines) >= 2:  # Ensure at least two samples for splitting
            # Assuming each line contains a preprocessed document
            train_docs, val_docs = train_test_split(lines, test_size=0.2, random_state=42)
            train_data.extend(train_docs)
            validation_data.extend(val_docs)
        else:
            print(f"Skipping file {train_file} as it contains only one sample")

# Concatenate the test data files
test_data = []
for test_file in test_files:
    with open(test_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        test_data.extend(lines)

# Example usage:
print("Number of documents in training set:", len(train_data))
print("Number of documents in validation set:", len(validation_data))
print("Number of documents in test set:", len(test_data))
