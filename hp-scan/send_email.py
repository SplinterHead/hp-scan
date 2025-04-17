import os
import smtplib
from datetime import datetime
from email.message import EmailMessage


def send_email_with_pdf(
    sender_email,
    receiver_email,
    subject,
    body,
    pdf_path,
    smtp_server,
    smtp_port,
    login,
    password,
):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at path: {pdf_path}")

    # Create the email message
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg["Date"] = datetime.today().strftime("%Y-%m-%d")
    msg.set_content(body)

    # Read and attach PDF
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()
        msg.add_attachment(
            pdf_data,
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path),
        )

    # Send the email
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(login, password)
        server.send_message(msg)

    print("Email sent successfully.")
