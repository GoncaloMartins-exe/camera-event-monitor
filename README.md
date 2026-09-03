# C240I ONVIF Event Monitor

Monitoriza eventos ONVIF (deteção de pessoas, intrusão, movimento, etc.)
de uma câmara IP via PullPoint Subscription.

## Configuração

1. Criar e ativar a venv:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. `pip install -r requirements.txt`
3. `python monitor.py`