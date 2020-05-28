import tabula


def extranct(saurce_row):
    return list(filter(
        lambda x: len(x) > 0,
        [[r for r in row if r['top'] > 103] for row in saurce_row]
        ))


df = tabula.read_pdf(
    "service_code.pdf",
    # guess=True,
    area=[
        [63.89, 38.12, 63.89+759.38, 38.12+145.69],
        [63.89, 498.24, 63.89+759.38, 498.24+61.31]
    ],
    lattice=True,
    multiple_tables=False,
    format="JSON",
    pages="3"
)

joined = []
for service, unit in zip(extranct(df[0]['data']), extranct(df[1]['data'])):
    joined.append([s['text'] for s in service] + [u['text'] for u in unit])

how = ""
for j in joined:
    if len(j) >= 5:
        how = j[4]
    else:
        j.append(how)
print(joined)
