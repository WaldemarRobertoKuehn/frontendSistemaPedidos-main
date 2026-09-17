# Aqui só nasce o app, entra o CORS e cada router é ligado com prefix e tags.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rotas.health import router as health_router
from rotas.itens import router as itens_router

app = FastAPI(title="Cardápio de pedidos")

# Libera o front-end React (outra porta) a chamar a API pelo navegador.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# O caminho das rotas não repete estes prefixos; eles ficam só aqui.
app.include_router(itens_router, prefix="/itens", tags=["itens"])
app.include_router(health_router, prefix="/health", tags=["health"])
