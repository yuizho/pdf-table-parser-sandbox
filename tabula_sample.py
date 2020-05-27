import tabula


df = tabula.read_pdf(
    "service_code.pdf",
    guess=True,
    lattice=True,
    format="JSON",
    pages="3"
)
print(df)
