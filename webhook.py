from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print("Received webhook data:", data)

        # Do something with the data here
        # Example: save to file, trigger another action, etc.

        return jsonify({"status": "success", "message": "Webhook received"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
