from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from database import get_offres, get_profils

def clean_text(df, text_cols):
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip().str.lower().fillna('')
    return df

def get_recommendations(student_name):
    offres_df = get_offres()
    profils_df = get_profils()

    # Renommer les colonnes en standard
    offres_df.columns = offres_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)
    profils_df.columns = profils_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)

    offres_df = offres_df.drop_duplicates()
    offres_df = offres_df.dropna(subset=["titre", "competence"])

    text_cols_offres = ["titre", "description", "competence"]
    text_cols_profils = ["nom", "filiere", "competences", "localisation_preferee", "domaine_souhaite"]  # adapte selon ta table `etudiants`

    offres_df = clean_text(offres_df, text_cols_offres)
    profils_df = clean_text(profils_df, text_cols_profils)

    # Chercher l'étudiant par nom
    student_row = profils_df[profils_df['nom'] == student_name.lower()]
    if student_row.empty:
        return {"error": "Étudiant non trouvé"}

    # Vectorisation des compétences
    all_skills = profils_df['competences'].tolist() + offres_df['competence'].tolist()
    vectorizer = TfidfVectorizer()
    vectorizer.fit(all_skills)

    X_students = vectorizer.transform(profils_df['competences'])
    X_offres = vectorizer.transform(offres_df['competence'])

    student_index = student_row.index[0]
    sim_scores = list(enumerate(cosine_similarity(X_students[student_index], X_offres)[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[:3]

    results = []
    for j, score in sim_scores:
        results.append({
            "titre": offres_df.iloc[j]['titre'],
            "description": offres_df.iloc[j]['description'],
            "score": round(score, 2)
        })
    return results
