import pandas as pd

print("El script ha iniciado correctamente.")
df = pd.read_csv("vehicles_us.csv")
print(df.head())