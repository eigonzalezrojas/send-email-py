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
attachment_path = os.getenv("FILE_PATH")  # Path to the attachment file


def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Onboarding 24-2B", sender_email))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Estimados(as),

        Carga de estudiantes al curso de Onboarding.
        
        Saludos.
        """
    )

    # Adjuntar archivo al correo
    if attachment_path:
        try:
            with open(attachment_path, 'rb') as file:
                file_data = file.read()
                file_name = Path(attachment_path).name
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        except Exception as e:
            print(f"Error al adjuntar el archivo: {e}")

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.send_message(msg)  # Using send_message instead of sendmail


if __name__ == "__main__":
    send_email(
        subject="Carga Onboarding",
        name="Eithel Gonzalez",
        receiver_email="eithelgonzalezrojas@gmail.com",
        due_date=datetime.date.today(),
        invoice_no="500",
        amount="5"
    )
