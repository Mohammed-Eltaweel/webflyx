from flask import Flask, render_template, redirect, request, jsonify
import requests
import os

app = Flask(__name__)

PADDLE_API_KEY = "5fd39c9ecba47509696dcc5da002b18713610d8832660f336b"
PADDLE_ENV = "sandbox"  # change to "production" later
PADDLE_API_URL = "https://sandbox-api.paddle.com" if PADDLE_ENV == "sandbox" else "https://api.paddle.com"

# Route: Home Page
@app.route("/")
def index():
    return render_template("index.html")

# Route: Create Checkout Link
@app.route("/create-checkout", methods=["POST"])
def create_checkout():
    headers = {
        "Authorization": f"Bearer {PADDLE_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "items": [{"price_id": "pri_01js6jka9hfqfqr6bpf6xzwv35", "quantity": 1}],
        "customer": {
            "email": "testuser@example.com"
        },
        "redirect_url": "http://localhost:5000/thank-you"
    }

    response = requests.post(f"{PADDLE_API_URL}/v1/checkouts", headers=headers, json=data)

    if response.status_code == 201:
        checkout_url = response.json()["data"]["url"]
        
        return jsonify({"url": checkout_url})
    else:
        
        return jsonify({"error": response.json()}), 400

# Route: Thank You Page
@app.route("/thank-you")
def thank_you():
    return "<h1>Payment Successful!</h1>"

# Webhook for Subscription Events
@app.route("/webhook", methods=["POST"])
def webhook():
    event = request.json
    print("Received Paddle Webhook:", event)
    # TODO: Verify webhook signature here
    # TODO: Activate user subscription in your DB
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(port=5000)
