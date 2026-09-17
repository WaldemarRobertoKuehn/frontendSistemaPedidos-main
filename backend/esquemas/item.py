# Esquema Pydantic de saída do recurso "item".
# Ele descreve o formato que a API devolve, para o /docs mostrar os campos certos.
from pydantic import BaseModel


class ItemSaida(BaseModel):
    id: int
    nome: str
    preco: float
    categoria: str
