from sqlalchemy import create_engine
import pandas as pd
import config

def get_connection():
    url = f"mysql+pymysql://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
                            
    return create_engine(url)

def get_offres():
    engine = get_connection()
    return pd.read_sql("SELECT * FROM offres", engine)

def get_profils():
    engine = get_connection()
    return pd.read_sql("SELECT * FROM etudiants", engine)
