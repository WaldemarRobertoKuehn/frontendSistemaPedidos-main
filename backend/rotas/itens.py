# Rotas do recurso "itens" do cardápio.
# Os dados ficam em lista na memória, neste mesmo arquivo, como visto na aula.
from fastapi import APIRouter, HTTPException

from esquemas.item import ItemSaida

router = APIRouter()

# Lista em memória com o cardápio desta aula (sem banco de dados).
cardapio = [
    {"id": 1, "nome": "Pizza Marguerita", "preco": 39.90, "categoria": "prato"},
    {"id": 2, "nome": "Suco de Laranja",  "preco": 12.50, "categoria": "bebida"},
]


# GET do recurso: o caminho não repete o prefixo "/itens", que fica no main.py.
@router.get("", response_model=list[ItemSaida])
def listar_itens(categoria: str | None = None):
    if categoria is None:
        return cardapio
    return [item for item in cardapio if item["categoria"] == categoria]


# GET de um item pelo id; devolve 404 quando o id não existe na lista.
@router.get("/{item_id}", response_model=ItemSaida)
def obter_item(item_id: int):
    for item in cardapio:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")
