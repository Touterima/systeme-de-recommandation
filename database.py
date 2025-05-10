from sqlalchemy import create_engine
import pandas as pd
import config

def get_connection():
    url = f"mysql+pymysql://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    return create_engine(url)

def get_offres():
    engine = get_connection()
    return pd.read_sql("SELECT id, titre, description, job_skills AS competence FROM offre_de_stage", engine)

def get_profils():
    engine = get_connection()
    return pd.read_sql("""
        SELECT id, name AS nom, major AS filiere, 
               skills AS competences, 
               preferred_location AS localisation_preferee, 
               desired_field AS domaine_souhaite 
        FROM etudiants
    """, engine)
