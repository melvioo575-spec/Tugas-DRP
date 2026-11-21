import pandas as pd

# 1. input dan pembacaan data
df = pd.read_csv("vgsales.csv")

print(df.shape)
print(df.head())

# 2. pembersihan data

# memeriksa data kosong
print(df.isna().sum())

# menghapus spasi berlebihan pada data
df["Name"]=df["Name"].str.strip()
df["Platform"]=df["Platform"].str.strip()
df["Genre"]=df["Genre"].str.strip()
df["Publisher"]=df["Publisher"].str.strip()

# menghapus baris yang memiliki Year dan Publisher yang kosong
df = df.dropna(subset=["Year","Publisher"])

# menghapus data duplikat
df = df.drop_duplicates()

# ringkasan statistik data
print(df.describe())

# melihat hasil setelah dibersihkan
print(df.shape)
print(df.head())
print(df.isna().sum())
print(df.duplicated().sum())

# menyimpan data yang sudah dibersihkan 
df.to_csv("vgsales_bersih.csv",index=False)
