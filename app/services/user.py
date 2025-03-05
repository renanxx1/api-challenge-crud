from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserService:
    """
    Serviço para gerenciamento de usuários no banco de dados.
    
    - Fornece métodos para obter, criar, atualizar e excluir usuários.
    - Utiliza SQLAlchemy para interação com o banco de dados.
    """
    
    def __init__(self, db: Session):
        """
        Inicializa o serviço com uma sessão do banco de dados.
        
        - **Parâmetros:**
            - `db` (Session): Sessão ativa do SQLAlchemy.
        """
        self.db = db


    def get_users(self):
        """
        Retorna todos os usuários cadastrados no banco de dados.
        
        - **Retorno:**
            - Lista de instâncias de `User`.
        """
        return self.db.query(User).all()


    def get_user(self, user_id: int):
        """
        Retorna um usuário específico com base no ID.
        
        - **Parâmetros:**
            - `user_id` (int): ID do usuário a ser buscado.
        - **Retorno:**
            - Instância de `User` ou `None` se não encontrado.
        """
        return self.db.query(User).filter(User.id == user_id).first()


    def create_user(self, user: UserCreate):
        """
        Cria um novo usuário no banco de dados.
        
        - **Parâmetros:**
            - `user` (UserCreate): Dados do novo usuário.
        - **Retorno:**
            - Instância de `User` criada.
        """
        db_user = User(name=user.name, email=user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user


    def update_user(self, user_id: int, user: UserCreate):
        """
        Atualiza os dados de um usuário existente.
        
        - **Parâmetros:**
            - `user_id` (int): ID do usuário a ser atualizado.
            - `user` (UserCreate): Novos dados do usuário.
        - **Retorno:**
            - Instância de `User` atualizada ou `None` se não encontrado.
        """
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.name = user.name
            db_user.email = user.email
            self.db.commit()
            self.db.refresh(db_user)
        return db_user


    def delete_user(self, user_id: int):
        """
        Remove um usuário do banco de dados.
        
        - **Parâmetros:**
            - `user_id` (int): ID do usuário a ser deletado.
        - **Retorno:**
            - Instância de `User` removida ou `None` se não encontrado.
        """
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return db_user