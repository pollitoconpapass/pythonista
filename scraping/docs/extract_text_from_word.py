from docx import Document


def get_text_from_word(file_path):
    doc = Document(file_path)
    full_text = ""

    for word in doc.paragraphs:
        full_text += word.text

    return full_text
