from fastapi import FastAPI, Request
import requests

app = FastAPI()

ACCESS_TOKEN = "APP_USR-5020467961877058-071222-37619cb73f2c32f45e3a5076e59a1eb3-290194608"

@app.post("/verificar")
async def verificar(request: Request):
    dados = await request.json()
    token = dados.get("token")
    if not token:
        return "DIE"

    payload = {
        "transaction_amount": round(random.uniform(0.10, 0.99), 2),
        "token": token,
        "description": "GG Checker",
        "installments": 1,
        "payer": {
            "email": "test@example.com"
        }
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    r = requests.post("https://api.mercadopago.com/v1/payments", json=payload, headers=headers)
    res = r.json()

    if res.get("status") == "approved":
        return "LIVE"
    else:
        return "DIE"
