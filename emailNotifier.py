import os
import sys
import smtplib
import ssl
from dotenv import load_dotenv

"""
Open a terminal and use the following if working on local

python -m smtpd -c DebuggingServer -n localhost:1025

Takes arguments .py (Reciever Email | Url)
"""
# Decision Booleans
onlineBOOL = False

# Get the login info from .env
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# Load the email
sender_email = os.getenv('USERNAME')
receiver_email = sys.argv[1]
url = sys.argv[2]
message = """\
Subject: Your Product is In-Stock!

Hello!

The product you have been looking for is now in stock.

Follow the link below to go buy it now!

""" + url


def main():
    # Determines the server and post used to send the emails.
    if onlineBOOL:
        server = "smtp.gmail.com"
        port = 465

        # Create a secure SSL context
        context = ssl.create_default_context()

        # login and send the email
        with smtplib.SMTP_SSL(server, port, context=context) as server:
            server.login(USERNAME, PASSWORD)
            server.sendmail(sender_email, receiver_email, message)
            print("E-mail has been sent online")
            server.close()
    else:
        server = "localhost"
        port = 1025  # For SSL

        # login and send the email
        with smtplib.SMTP(server, port) as server:
            server.sendmail(sender_email, receiver_email, message)
            print("E-mail has been sent offline")
            server.close()


if __name__ == "__main__":
    main()
