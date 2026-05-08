import requests
import time
import re
from datetime import datetime

# === CONFIG RENDER - TOKEN FALSO PA' GITHUB ===
TELEGRAM_TOKEN = "0000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
TELEGRAM_CHAT_ID = "000000000"

QUERIES = [
    'filename:electrum-4.5.8-setup.exe -user:spesmilo',
    'filename:electrum-4.6.0-setup.exe -user:spesmilo',
    'electrum phishing exe',
    'electrum fake wallet download',
    'electrum malware github',
    'electrumm.org setup'
]

def telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "HTML"}
    try:
        requests.post(url, data=data, timeout=10)
    except:
        pass

def scan_github():
    headers = {'User-Agent': 'HYDRA-Capa8'}
    for query in QUERIES:
        url = f"https://api.github.com/search/repositories?q={query}&sort=updated"
        try:
            r = requests.get(url, headers=headers, timeout=15).json()
            for repo in r.get('items', [])[:2]:
                repo_url = repo['html_url']
                print(f"👁️ Revisando: {repo_url}")
                if 'electrum' in repo_url.lower() and 'spesmilo' not in repo_url:
                    msg = f"🚨 <b>SPOOF DETECTADO</b>\n{repo_url}\nHora: {datetime.now()}"
                    print(msg)
                    telegram(msg)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2)

print("🔥 HYDRA V3.0 RENDER ONLINE")
telegram("🔥 <b>HYDRA 24/7 ONLINE</b>\nCapa 8 desde Render")

while True:
    print(f"\n[{datetime.now()}] Iniciando ciclo de caza...")
    scan_github()
    print("Durmiendo 300s...")
    time.sleep(300)