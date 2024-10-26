import os
import gensim.models

# Function to load the pre-trained Doc2Vec model
def load_model():
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, 'dart.doc2vec')

    # Load the saved Doc2Vec model
    model = gensim.models.Doc2Vec.load(model_path)
    return model

# Function to get similar books based on user input (ISBN-13 and description)
def get_similar_books(isbn13, description):
    # Load the model
    model = load_model()
    
    # Process the input description using the same preprocessing as during training
    user_input_vector = model.infer_vector(description.split())
    
    # Find the top 5 most similar documents (books) based on the input vector
    similar_books = model.dv.most_similar([user_input_vector], topn=5)
    
    # Extract the ISBN-13s from the similar_books
    similar_isbns = [book[0] for book in similar_books]
    
    return similar_isbns
