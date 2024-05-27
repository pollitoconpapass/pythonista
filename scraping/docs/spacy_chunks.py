import spacy # -> Specialized NLP library


def generate_chunks(text):
    nlp = spacy.load("en_core_web_sm")  # -> English model  
    doc = nlp(text)
    sentences = list(doc.sents)

    return sentences
