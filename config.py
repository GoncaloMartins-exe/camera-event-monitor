import os
from dotenv import load_dotenv

load_dotenv()

IP = os.getenv("CAMERA_IP")
PORT = int(os.getenv("CAMERA_PORT", "80"))
USER = os.getenv("CAMERA_USER")
PASSWORD = os.getenv("CAMERA_PASSWORD")

if not all([IP, USER, PASSWORD]):
    raise RuntimeError(
        "Faltam variáveis no .env: CAMERA_IP, CAMERA_USER ou CAMERA_PASSWORD"
    )

BASE_URL = f"http://{IP}:{PORT}/onvif/service"
RECONNECT_DELAY = 3
REQUEST_TIMEOUT = 15