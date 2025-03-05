from sqlalchemy import Column, Integer, String
from app.db.session import Base

class User(Base):
    """
    Modelo de dados para a entidade User.
    
    Representa a tabela `users` no banco de dados.
    
    - **id** (int): Identificador único do usuário.
    - **name** (str): Nome do usuário.
    - **email** (str): Endereço de e-mail do usuário (único).
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
