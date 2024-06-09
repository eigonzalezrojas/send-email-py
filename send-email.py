import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
import datetime

from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = 'smtp-mail.outlook.com'

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read enviroment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Onboarding 24-2B", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
            Estimados(as)
            Informo que la carga del día de hoy {due_date} tuvo {invoice_no}
        """
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    send_email(
        subject="Carga Onboarding",
        name = "Eithel Gonzalez",
        receiver_email= "eithelgonzalezrojas@gmail.com",
        due_date= datetime.date.today(),
        invoice_no="500",
        amount="5"
    )