import fitz


def extract_text_from_pdf(pdf_path, start, end):
    doc = fitz.open(pdf_path)
    text = ""

    for i in doc[start:end]:
        text += i.get_text()
    
    return text
