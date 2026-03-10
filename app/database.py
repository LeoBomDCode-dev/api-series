from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv 
from dotenv import load_dotenv

load_dotenv()

# SERVER_URL = DATABASE_URL = f"""mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@
# {getenv('DB_HOST')}"""

SERVER_URL = "mysql+pymysql://root:admin@localhost" 

engine_server = create_engine(SERVER_URL)

with engine_server.connect() as conn:
    conn.execute(text(f'CREATE DATABASE IF NOT EXISTS series_api'))
    conn.commit()


# DATABASE_URL = "mysql+pymysql://root:admin@localhost/series_api"
# DATABASE_URL = f"""mysql+pymysql://{getenv('DB_USER')}:{getenv("DB_PSWD")}@
# {getenv('DB_HOSt')}/{getenv('DB_NAME')}"""')

DATABASE_URL = "mysql+pymysql://root:admin@localhost/series_api"

# Criar um "motor" que fará o gerenciamento da conexão
engine = create_engine(DATABASE_URL)

#criando uma sessão para executar os comandos SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria um objeto da base de dados manipulavel pelo python
Base = declarative_base()

# Injeção de independencia: injeta a sessão do banco de dados
# em cada rota que for criada. 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()