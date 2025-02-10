import os
import time
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Cargamos credenciales
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_PHONE = os.getenv("MY_PHONE")
TO_PHONE = os.getenv("TO_PHONE")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_message(content):
    message = client.messages.create(
        from_=f'whatsapp:{MY_PHONE}',
        to=f'whatsapp:{TO_PHONE}',
        body=content
    )
    time.sleep(3)  # Damos tiempo para que se actualice el estado del mensaje
    status = client.messages.get(message.sid).fetch().status

    if status in ["sent", "delivered", "read"]:
        print("✅ Mensaje enviado con éxito.")
    else:
        print(f"❌ Error enviando mensaje. Estado: {status}")
