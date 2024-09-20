from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/webhook/")
@app.get("/webhook/")
async def webhook_whatsapp(request: Request):
    if request.method == "GET":
        params = request.query_params
        if params.get('hub.verify_token') == "SportsLab":
            return params.get('hub.challenge')
        else:
            return JSONResponse(content={"detail": "Error de autenticación"}, status_code=401)
    
    data = await request.json()
    # Extraemos el número de teléfono y el mensaje
    mensaje = f"Telefono: {data['entry'][0]['changes'][0]['value']['messages'][0]['from']}"
    mensaje += f" [Mensaje: {data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']}]"

    # Escribimos el número de teléfono y el mensaje en el archivo de texto
    with open("texto.txt", "w") as f:
        f.write(mensaje)
    
    return JSONResponse(content={"status": "success"}, status_code=200)