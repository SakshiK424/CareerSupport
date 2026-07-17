import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    text = ""

    # Open the uploaded PDF
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    # Read every page
    for page in doc:
        text += page.get_text()

    return text