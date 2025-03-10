from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined responses based on keywords
responses = {
    "hello": "Hello! How can I assist you with your travel plans?",
    "tour packages": "We offer various tour packages, including beach, adventure, and cultural trips.",
    "hotel booking": "We provide hotel booking services with special discounts. Let me know your preferred location.",
    "contact": "You can reach us at support@tourism.com or call +91-9876543210.",
    "bye": "Goodbye! Have a great day and happy travels!"
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    
    # Find a response based on keywords
    for key in responses.keys():
        if key in user_message:
            return jsonify({"reply": responses[key]})

    return jsonify({"reply": "I'm sorry, I didn't understand that. Can you rephrase?"})

if __name__ == "__main__":
    app.run(debug=True)
