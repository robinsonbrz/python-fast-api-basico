# pip install fastapi
# pip install uvicorn

# rodando 
# uvicorn main:app --reload

from fastapi import FastAPI
from pydantic import BaseModel


def usuario_existe(id_usuario):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario
    return {"Status":404, "Mensagem": "Não encontrou usuario"}


app = FastAPI()

# rota Raiz
@app.get("/")
def raiz():
    return {"Olá": "mundo!"}


# model
class Usuario(BaseModel):
    id: int
    email: str
    senha: str


# Criar base de dados
base_de_dados = [
    Usuario(id=1, email="roger@roger.com", senha="roger123"),
    Usuario(id=2, email="teste@roger.com", senha="teste123")
]

# Rota Get All
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota Get Id
@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int): # definir o tipo para não haver erro
    return usuario_existe(id_usuario)

# Rota Insere
@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    # importante criar regras de negocio ex: duplicidade
    print(type(usuario))
    base_de_dados.append(usuario)
    return usuario

# Rota Delete Id
@app.delete("/usuarios/{id_usuario}")
def delete_item(id_usuario: int):
    usuario = usuario_existe(id_usuario)
    if isinstance(usuario, Usuario):
        base_de_dados.remove(usuario)
        return {'Message': f'Usuário id: {usuario.id} deletado'}
    return usuario


# Rota Edit Id

