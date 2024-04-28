import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

# Download NLTK resources TO BE RUN ONE TIME ONLY FOR FIRST TIME DURING CODE EXECUTION
# nltk.download('punkt')
# nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text.lower())  # Convert text to lowercase and tokenize
    
    # Remove punctuation and non-alphanumeric characters
    tokens = [re.sub(r'[^a-zA-Z0-9]', '', token) for token in tokens if token.isalnum()]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    
    return tokens


files =[
    "dis&symp_test_1.txt",
    "dis&symp_test_2.txt",
    "dis&symp_test_3.txt",
    "dis&symp_train_1.txt",
    "dis&symp_train_2.txt",
    "dis&symp_train_3.txt",
    "dis&symp_train_4.txt",
    "dis&symp_train_5.txt",
    "dis&symp_train_6.txt",
    "dis&symp_train_7.txt",
    "dis&symp_train_8.txt",
    "dis&symp_train_9.txt",
    "dis&symp_train_10.txt",
    "dis&symp_train_11.txt",
    "dis&symp_train_12.txt",
    "sci&edu_test_1.txt",
    "sci&edu_test_2.txt",
    "sci&edu_test_3.txt",
    "sci&edu_train_1.txt",
    "sci&edu_train_2.txt",
    "sci&edu_train_3.txt",
    "sci&edu_train_4.txt",
    "sci&edu_train_5.txt",
    "sci&edu_train_6.txt",
    "sci&edu_train_7.txt",
    "sci&edu_train_8.txt",
    "sci&edu_train_9.txt",
    "sci&edu_train_10.txt",
    "sci&edu_train_11.txt",
    "sci&edu_train_12.txt",
    "sports_test_1.txt",
    "sports_test_2.txt",
    "sports_test_3.txt",
    "sports_train_1.txt",
    "sports_train_2.txt",
    "sports_train_3.txt",
    "sports_train_4.txt",
    "sports_train_5.txt",
    "sports_train_6.txt",
    "sports_train_7.txt",
    "sports_train_8.txt",
    "sports_train_9.txt",
    "sports_train_10.txt",
    "sports_train_11.txt",
    "sports_train_12.txt",
]

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as file:
        # Read the entire content of the file
        file_content = file.read()

    # Split the file content into separate documents based on newline characters
    documents = file_content.split("\n\n")  # Adjust the delimiter based on your file format

    # Preprocess each document
    preprocessed_documents = [preprocess_text(document) for document in documents]

    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    for i, preprocessed_doc in enumerate(preprocessed_documents):
        # Construct the output file path with "p_" prefix and document index
        output_file_path = f"p_{file_name}.txt"

        # Write preprocessed data to a separate file
        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(" ".join(preprocessed_doc) + "\n")

        print("Preprocessed data saved to:", output_file_path)
