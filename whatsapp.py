# This file contains the logic to send WhatsApps with the info
from twilio.rest import Client
from dotenv import load_dotenv
import os
import time
from newsAPI import form_message

# Cargamos las variables desde .env
load_dotenv()

# Obtenemos las credenciales desde var de entorno
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_phone = os.getenv("MY_PHONE")
to_phone = os.getenv("TO_PHONE")

# Creamos la cuenta cliente con el accountsid y el authtoken
client = Client(account_sid, auth_token)

content = form_message()

# Enviamos el mensaje
message = client.messages.create(
  from_=f'whatsapp:{my_phone}',
  to=f'whatsapp:{to_phone}',
  body=f"{content}"
)

# Esperamos 3s para que el message_status se actualice
time.sleep(3)

message = client.messages.get(message.sid).fetch()
message_status = message.status

# Verificar si se envió correctamente
if message_status in ["sent", "delivered", "read"]:
    print("✅ Mensaje enviado con éxito.")
else:
    print(f"❌ No se pudo enviar el mensaje. Estado: {message_status}")
