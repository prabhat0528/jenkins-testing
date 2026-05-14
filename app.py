from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is home"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    print(request.data)
    return "Webhook received", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2002)