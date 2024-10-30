from flask import Flask, jsonify, request
import random
import json
import os

app = Flask(__name__)

file_path = 'dog_quotes.json'

# Load or initialize quotes
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        quotes = json.load(file)
else:
    print("#file does not exist, please check the quotes.json file")
    quotes = []

def save_quotes():
    with open(file_path, 'w') as file:
        json.dump(quotes, file)

# Read: Get a random quote
@app.route("/quote", methods=["GET"])
def get_random_quote():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

# Retrieve all quotes with indexes
@app.route("/quotes", methods=["GET"])
def get_all_quotes():
    indexed_quotes = {index: quote for index, quote in enumerate(quotes)}
    return jsonify(indexed_quotes)

# Create: Add a new quote
@app.route("/quote", methods=["POST"])
def add_quote():
    new_quote = request.json.get("quote")
    if new_quote:
        quotes.append(new_quote)
        save_quotes()
        return jsonify({"message": "Quote added.", "quotes": quotes}), 201
    return jsonify({"error": "Please provide a quote."}), 400

# Update: Update a quote by index
@app.route("/quote/<int:index>", methods=["PUT"])
def update_quote(index):
    if 0 <= index < len(quotes):
        updated_quote = request.json.get("quote")
        if updated_quote:
            quotes[index] = updated_quote
            save_quotes()
            return jsonify({"message": f"Quote at index {index} updated.", "quote": quotes[index]})
        return jsonify({"error": "Please provide a new quote."}), 400
    return jsonify({"error": "Index out of range."}), 404

# Delete: Remove a quote by index
@app.route("/quote/<int:index>", methods=["DELETE"])
def delete_quote(index):
    if 0 <= index < len(quotes):
        deleted_quote = quotes.pop(index)
        save_quotes()
        return jsonify({"message": f"Quote deleted: {deleted_quote}", "quotes": quotes})
    return jsonify({"error": "Index out of range."}), 404

if __name__ == "__main__":
    app.run(debug=True)
