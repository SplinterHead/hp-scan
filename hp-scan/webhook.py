from dotenv import load_dotenv
from flask import Flask, jsonify, request
from scan import do_scan

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        data = request.json
        print("Received webhook data:", data)

        do_scan()

        # Do something with the data here
        # Example: save to file, trigger another action, etc.

        return jsonify({"status": "success", "message": "Webhook received"}), 200


load_dotenv()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
