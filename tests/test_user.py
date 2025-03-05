"""
Módulo de testes para a API de usuários utilizando FastAPI e pytest.

Testes incluídos:
- Criar um usuário (`POST /users`)
- Listar todos os usuários (`GET /users`)
- Buscar um usuário específico (`GET /users/{user_id}`)
- Atualizar um usuário (`PUT /users/{user_id}`)
- Deletar um usuário (`DELETE /users/{user_id}`)
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    """
    Testa a criação de um usuário na API.

    - Envia um `POST /users` com um novo usuário.
    - Verifica se o status de resposta é 200 (OK).
    - Verifica se o nome do usuário retornado corresponde ao enviado.
    """
    response = client.post("/users", json={"name": "Usuario Teste", "email": "usuario_teste@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Usuario Teste"


def test_read_users():
    """
    Testa a listagem de todos os usuários cadastrados.

    - Envia um `GET /users`.
    - Verifica se o status de resposta é 200 (OK).
    """
    response = client.get("/users")
    assert response.status_code == 200


def test_read_user():
    """
    Testa a busca de um usuário específico pelo ID.

    - Envia um `GET /users/1`.
    - Verifica se o status de resposta é 200 (OK).
    """
    response = client.get("/users/1")
    assert response.status_code == 200


def test_update_user():
    """
    Testa a atualização dos dados de um usuário.

    - Envia um `PUT /users/1` com um novo nome e e-mail.
    - Verifica se o status de resposta é 200 (OK).
    """
    response = client.put("/users/1", json={"name": "Usuario Teste Editado", "email": "usuario_teste@example.com"})
    assert response.status_code == 200


def test_delete_user():
    """
    Testa a remoção de um usuário pelo ID.

    - Envia um `DELETE /users/1`.
    - Verifica se o status de resposta é 200 (OK).
    """
    response = client.delete("/users/1")
    assert response.status_code == 200
