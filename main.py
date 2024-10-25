import smtplib
from info import password, email, recipients, subject, body
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_email(subject: str, body: str, sender_email: str, attachment_path: str) -> MIMEMultipart:
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))
    attach_file(message, attachment_path)

    return message

def attach_file(message: MIMEMultipart, file_path: str) -> None:
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename={file_path.split('/')[-1]}",
    )

    message.attach(part)

def send_email(sender_email: str, sender_password: str, recipient_email: str, message: MIMEMultipart) -> None:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

def main():
    sender_email = email
    sender_password = password
    recipients_emails = recipients
    subject_to_send = subject
    body_to_send = body
    attachment_path = "Marvin_Siri_Resume.pdf"

    # Create the email
    for recipient in recipients_emails:
        message = create_email(subject_to_send, body_to_send, sender_email, attachment_path)
        message["To"] = recipient

        # Send the email
        send_email(sender_email, sender_password, recipient, message)

    print("Emails sent successfully.")

if __name__ == "__main__":
    main()
