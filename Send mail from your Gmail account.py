from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Email content
MAIL_CONTENT = """
    iopdsfhgfoufdoigofdsihdhfuogrsfdoiofds[hifdsh]
    """

# Sender and receiver email addresses
SENDER_ADDRESS = "xxxxx@gmail.com"
SENDER_PASS = "4415"
RECEIVER_ADDRESS = "yyyyy@gmail.com"


def send_email(sender_address, sender_pass, receiver_address, mail_content):
    # Construct the email message
    message = MIMEMultipart()
    message["From"] = sender_address
    message["To"] = receiver_address
    message["Subject"] = "A test mail sent by Python. It has an attachment."
    message.attach(MIMEText(mail_content, "plain"))

    # Setup SMTP session for sending the mail
    try:
        with smtplib.SMTP("smtp.gmail.com") as session:
            session.starttls()
            session.login(user=sender_address, password=sender_pass)

            text = message.as_string()
            # Send the email
            session.sendmail(sender_address, receiver_address, text)
            print("Mail Sent")
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function to send the email
if __name__ == "__main__":
    send_email(
        sender_address=SENDER_ADDRESS,
        sender_pass=SENDER_PASS,
        receiver_address=RECEIVER_ADDRESS,
        mail_content=MAIL_CONTENT,
    )
