import spacy
import nltk
nltk.download('punkt')

nlp = spacy.load("en_core_web_sm")

def extract_resume_details(text: str):
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ in ["SKILL", "TECHNOLOGY"]]
    return {"skills": skills, "experience": extract_experience(text)}

def extract_experience(text: str):
    sentences = nltk.sent_tokenize(text)
    return [sent for sent in sentences if "years" in sent.lower()]
