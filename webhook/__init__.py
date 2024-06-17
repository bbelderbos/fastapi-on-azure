import fastapi

app = fastapi.FastAPI()

@app.post("/webhook")
async def webhook(payload: dict):
    """
    Simple webhook that just returns the payload.
    Normally you would do something with the payload here.
    And add some security like secret key validation (HMAC for example).
    """
    return {"status": "ok", "payload": payload}
