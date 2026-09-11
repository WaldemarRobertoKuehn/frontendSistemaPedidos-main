from fastapi import FastAPI

app = FastAPI(title="Cardápio de pedidos")

@app.get("/health")
def health():
    return {"status": "ok"}
