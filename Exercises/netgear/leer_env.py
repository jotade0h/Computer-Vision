from dotenv import load_dotenv
import os

# 🔄 Cargar variables desde .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# 📥 Leer variables
user = os.getenv("CAMERA_USER")
password = os.getenv("CAMERA_PASSWORD")
url = os.getenv("CAMERA_URL")

# 📤 Mostrar resultados
print("📦 Variables cargadas:")
print(f"👤 Usuario: {user}")
print(f"🔑 Contraseña: {password}")
print(f"📷 URL: {url}")

# Verificación de carga
if not url:
    print("⚠️  La variable CAMERA_URL no fue encontrada.")
