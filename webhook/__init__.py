import azure.functions as func

from fastapi import FastAPI

app = FastAPI()


@app.post("/webhook")
async def webhook(payload: dict) -> dict:
    """
    Simple webhook that just returns the payload.
    Normally you would do something with the payload here.
    And add some security like secret key validation (HMAC for example).
    """
    return {"status": "ok", "payload": payload}


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
