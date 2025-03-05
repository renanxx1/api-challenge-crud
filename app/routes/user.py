from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import database 
from app.services.user import UserService
from app.schemas.user import UserCreate, UserResponse

# Cria uma rota para a entidade "Users"
router = APIRouter(prefix="/users", tags=["Users"])

def get_user_service(db: Session = Depends(database.get_db)):
    """
    Dependência para fornecer uma instância do UserService.
    
    - **Parâmetros:**
        - `db` (Session): Sessão ativa do banco de dados.
    - **Retorno:**
        - Instância de `UserService`.
    """
    return UserService(db)


@router.get("/", response_model=list[UserResponse])
def read_users(user_service: UserService = Depends(get_user_service)):
    """
    Retorna a lista de todos os usuários cadastrados no banco de dados.

    - **Retorno:**
        - Lista de usuários no formato `UserResponse`.
    """
    return user_service.get_users()


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    """
    Retorna os detalhes de um usuário específico com base no ID.

    - **Parâmetros:**
        - `user_id` (int): ID do usuário a ser buscado.
    - **Erros possíveis:**
        - `404 Not Found`: Se o usuário não for encontrado.
    - **Retorno:**
        - Um objeto `UserResponse` com os dados do usuário.
    """
    db_user = user_service.get_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    """
    Cria um novo usuário no banco de dados.

    - **Parâmetros:**
        - `user` (UserCreate): Objeto contendo `name` e `email` do novo usuário.
    - **Retorno:**
        - Um objeto `UserResponse` com os dados do usuário recém-criado.
    """
    return user_service.create_user(user)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, user_service: UserService = Depends(get_user_service)):
    """
    Atualiza os dados de um usuário existente.

    - **Parâmetros:**
        - `user_id` (int): ID do usuário a ser atualizado.
        - `user` (UserCreate): Objeto contendo os novos valores de `name` e `email`.
    - **Erros possíveis:**
        - `404 Not Found`: Se o usuário não for encontrado.
    - **Retorno:**
        - Um objeto `UserResponse` atualizado.
    """
    db_user = user_service.update_user(user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}")
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    """
    Remove um usuário do banco de dados com base no ID.

    - **Parâmetros:**
        - `user_id` (int): ID do usuário a ser deletado.
    - **Erros possíveis:**
        - `404 Not Found`: Se o usuário não for encontrado.
    - **Retorno:**
        - Mensagem confirmando a exclusão do usuário.
    """
    db_user = user_service.delete_user(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
