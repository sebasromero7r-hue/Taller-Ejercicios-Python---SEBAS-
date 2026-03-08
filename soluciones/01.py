import pandas as pd


df = pd.read_csv("data/personas.csv")


ids_no_numericos = df["id"].astype(str).str.contains(r"\D")

cantidad = ids_no_numericos.sum()

print("Filas con id no numérico:", cantidad)
