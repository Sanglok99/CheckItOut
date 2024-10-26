from flask import Flask, request, jsonify
from models.topic_model import get_similar_books

app = Flask(__name__)

# 기본 라우트 (테스트용)
@app.route('/')
def home():
    return "Welcome to the Book Recommendation Service!(in the server)"

# 도서 추천 라우트 (POST 요청)
@app.route('/recommend', methods=['POST'])
def recommend():
   # Get JSON data from the Flutter frontend
    data = request.json
    isbn13 = data.get('isbn13')
    description = data.get('description')
    
    if not isbn13 or not description:
        return jsonify({"error": "Invalid input"}), 400

    # Use your AI model to find similar books
    similar_books = get_similar_books(isbn13, description)  # Returns a list of ISBN-13s
    
    # Return the list of similar book ISBN-13s to the frontend
    return jsonify({"similar_books": similar_books})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
