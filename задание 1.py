import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")

print(df.head(10))
print(f"Размерность данных: {df.shape}")
print(f"Количество пустых значений в каждом столбце: {df.isnull().sum()}")
print(f"Типы данных: \n {df.dtypes}")