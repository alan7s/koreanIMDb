import pandas as pd
df = pd.read_csv("koreanTitles.csv")
print(df.drop_duplicates(subset=['ID']).shape)
dx = df.drop_duplicates(subset=['ID'])
dx.to_csv('semDuplicados.csv', index=False, encoding='utf-8')