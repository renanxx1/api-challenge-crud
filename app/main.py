from fastapi import FastAPI
from app.routes import user, health
from app.db.session import database

# Criando a aplicação FastAPI
app = FastAPI(
    title="Desafio PicPay",
    description="API para gerenciamento de usuários com FastAPI e SQLite",
    version="1.0"
)

# Cria tabelas caso não exista durante inicialização
@app.on_event("startup")
def startup_event():
    database.create_tables()

# Incluindo rotas na aplicação
app.include_router(user.router)

# Rota de healthcheck
app.include_router(health.router)