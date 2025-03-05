from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./users.db"

class DatabaseSession:
    """
    Classe que gerencia a conexão com o banco de dados usando SQLAlchemy.
    
    - Cria a engine do banco de dados.
    - Gerencia a sessão do banco.
    - Permite a criação das tabelas.
    """
    
    def __init__(self, database_url: str = DATABASE_URL):
        """
        Inicializa a conexão com o banco de dados.

        - **Parâmetros:**
            - `database_url` (str): URL do banco de dados.
        """
        self.engine = create_engine(database_url, connect_args={"check_same_thread": False})
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()


    def create_tables(self):
        """
        Cria as tabelas no banco de dados caso não existam.
        
        - **Executa:** `Base.metadata.create_all(bind=self.engine)`
        """
        self.Base.metadata.create_all(bind=self.engine)
    
    
    def get_db(self):
        """
        Obtém uma sessão do banco de dados.
        
        - **Uso:** Utilizado como dependência no FastAPI.
        - **Garante:** Que a sessão seja fechada corretamente após o uso.
        
        - **Retorno:** Um gerador que fornece uma instância de `Session`.
        """
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


# Criamos uma instância global da classe para ser reutilizada
database = DatabaseSession()
#database.create_tables()
Base = database.Base