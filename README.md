# API CRUD - API de Usuários

Este projeto é uma API de gerenciamento de usuários utilizando **FastAPI** e **SQLite**, seguindo boas práticas de arquitetura e organização de código.

## 📂 Estrutura do Projeto

```

│── app/
│   │   ├── routes/           # Módulo de rotas
│   │   │   ├── user.py       # Rotas de usuário
│   ├── db/                   # Banco de dados
│   │   ├── session.py        # Configuração do banco de dados e conexão
│   ├── models/               # Modelos do banco de dados
│   │   ├── user.py           # Modelo de usuário (SQLAlchemy)
│   ├── schemas/              # Schemas de validação Pydantic
│   │   ├── user.py           # Schema de usuário
│   ├── services/             # Serviços para regras de negócios
│   │   ├── user.py           # Lógica de usuários encapsulada
│   ├── main.py               # Arquivo principal da aplicação
│── tests/                    # Testes automatizados
│   ├── test_users.py         # Testes para a API de usuários
│── .gitignore                # Arquivos ignorados pelo Git
│── requirements.txt          # Dependências do projeto
│── README.md                 # Documentação do projeto
```

---

## 🚀 Como Rodar o Projeto

### 1️⃣ Criar e ativar o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar as dependências:

```bash
pip install -r requirements.txt
```

### 3️⃣ Rodar a aplicação:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔗 Endpoints da API

### 📌 Criar um usuário

```http
POST /users
```

#### Corpo da requisição (JSON):

```json
{
  "name": "Nome do Usuario",
  "email": "email@example.com"
}
```

### 📌 Listar todos os usuários

```http
GET /users
```

### 📌 Buscar um usuário por ID

```http
GET /users/{user_id}
```

### 📌 Atualizar um usuário

```http
PUT /users/{user_id}
```

#### Corpo da requisição (JSON):

```json
{
  "name": "Usuario X",
  "email": "usuario_x@example.com"
}
```

### 📌 Deletar um usuário

```http
DELETE /users/{user_id}
```

---

## 🧪 Como Rodar os Testes

Para executar os testes unitários:

```bash
pytest tests/
```

---

## 📌 Tecnologias Utilizadas

✅ **FastAPI** - Framework para APIs rápidas e assíncronas
✅ **SQLite** - Banco de dados leve e fácil de configurar
✅ **SQLAlchemy** - ORM para interagir com o banco de dados
✅ **Pydantic** - Validação e serialização de dados
✅ **Pytest** - Framework de testes

---
