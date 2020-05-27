import pdfplumber

with pdfplumber.open("service_code.pdf") as pdf:
    page = pdf.pages[2]
    print(page.extract_tables())
