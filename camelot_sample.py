import camelot

table = camelot.read_pdf(
    filepath="service_code.pdf",
    pages="1-30",
    split_text=True
)
print(table)
