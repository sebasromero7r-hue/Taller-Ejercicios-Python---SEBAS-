import pandas as pd
import codecs


df = pd.read_csv("data/personas.csv")

df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

cantidad_maria = (df["nombre"].str.strip().str.title() == "Maria").sum()

print("Cantidad de personas llamadas Maria:", cantidad_maria)