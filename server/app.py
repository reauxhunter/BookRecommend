from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Allow frontend (React) to access backend

# Load the dataset when the app starts
try:
    books = pd.read_csv("books.csv")
    books = books[['book_id', 'title', 'authors', 'average_rating']]
    books = books.dropna().reset_index(drop=True)
except Exception as e:
    print(f"Error loading books.csv: {e}")
    books = pd.DataFrame(columns=['book_id', 'title', 'authors', 'average_rating'])

@app.route("/")
def home():
    return jsonify({"message": "Book recommender backend is running!"})

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books.head(50).to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
