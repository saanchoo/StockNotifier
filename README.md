# StockNotifier

StockNotifier es una aplicación que monitorea el mercado de valores y criptomonedas, enviando notificaciones cuando hay cambios significativos en el precio de una acción o criptomoneda. Si el cambio supera un umbral determinado, el sistema recupera noticias relevantes y las envía a través de WhatsApp.

## 🚀 Características

- Obtiene el cambio porcentual en el precio de una acción o criptomoneda.
- Recupera noticias relevantes si el cambio supera un umbral.
- Envía notificaciones por WhatsApp con los datos de la variación y las noticias más recientes.

## 📦 Instalación

### 1. Clona el repositorio:
```bash
 git clone https://github.com/saanchoo/stockTrader.git
 cd stockTrader
```

### 2. Crea y activa un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate  # En Windows
```

### 3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuración

1. **Configura las claves API** en un archivo `.env` en la raíz del proyecto:
```
ALPHA_VANTAGE_API_KEY=TU_CLAVE_AQUI
NEWS_API_KEY=TU_CLAVE_AQUI
TWILIO_ACCOUNT_SID=TU_CLAVE_AQUI
TWILIO_AUTH_TOKEN=TU_CLAVE_AQUI
TWILIO_PHONE_NUMBER=+TU_NUMERO
MY_PHONE_NUMBER=+TU_NUMERO
```
2. **Asegúrate de tener acceso a la API de Twilio para WhatsApp** y configurar el sandbox.

## ▶️ Uso

Ejecuta el script principal:
```bash
python main.py
```

Si hay una variación significativa en el precio de la acción o criptomoneda monitoreada, recibirás un mensaje de WhatsApp con la información.

## 🛠 Estructura del Proyecto
```
StockNotifier/
│── stocksAPI.py      # Obtiene el cambio de precios de acciones o criptos
│── newsAPI.py        # Obtiene noticias relevantes
│── whatsapp.py       # Envía mensajes de WhatsApp
│── main.py           # Orquesta todo el flujo
│── requirements.txt  # Dependencias del proyecto
│── .env              # Variables de entorno (ignorado en git)
│── README.md         # Documentación del proyecto
```

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT.

---
📩 **Autor:** [@saanchoo](https://github.com/saanchoo)
