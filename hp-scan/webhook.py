import os
import threading
import uuid
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from scan import do_scan
from send_email import send_email_with_pdf

app = Flask(__name__)


def _scan_and_email():
    DATETIME = datetime.now()
    FILENAME = uuid.uuid4()

    do_scan(filename=str(FILENAME))

    send_email_with_pdf(
        sender_email=os.getenv("SMTP_SENDER_EMAIL"),
        receiver_email=os.getenv("SMTP_RECIEVER_EMAIL"),
        subject="Scanned Document",
        body=f"Document scanned at {DATETIME}",
        pdf_path=f"{FILENAME}.pdf",
        smtp_server=os.getenv("SMTP_SERVER"),
        smtp_port=os.getenv("SMTP_SERVER_PORT", 465),
        login=os.getenv("SMTP_SENDER_EMAIL"),
        password=os.getenv("SMTP_SENDER_PASSWORD"),
    )


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        data = request.json
        print("Received webhook data:", data)

        thread = threading.Thread(target=_scan_and_email)
        thread.start()

        return jsonify({"status": "success", "message": "Webhook received"}), 200


load_dotenv()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
