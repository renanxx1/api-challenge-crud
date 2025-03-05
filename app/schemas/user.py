from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """
    Esquema base para a entidade User.
    
    - **name** (str): Nome do usuário.
    - **email** (EmailStr): Endereço de e-mail do usuário, validado automaticamente.
    """
    name: str
    email: EmailStr 

class UserCreate(UserBase):
    """
    Esquema para criação de um novo usuário.
    
    Herda de `UserBase` e não adiciona novos atributos.
    """
    pass

class UserResponse(UserBase):
    """
    Esquema para resposta de um usuário já cadastrado.
    
    - **id** (int): Identificador único do usuário.
    """
    id: int

    class Config:
        """
        Configuração do Pydantic para compatibilidade com SQLAlchemy.
        """
        from_attributes = True  # Garante compatibilidade com SQLAlchemy