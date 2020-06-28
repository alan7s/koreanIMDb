import pandas as pd
df1 = pd.read_csv("koreanTitles.csv")
df2 = pd.read_csv("koreanTitles2.csv")
print(df1.drop_duplicates(subset=['ID']).shape)
print(df2.drop_duplicates(subset=['Title']).shape)
dx1 = df1.drop_duplicates(subset=['ID'])
dx2 = df2.drop_duplicates(subset=['Title'])
dx1.to_csv('koreanTitles.csv', index=False, encoding='utf-8')
dx2.to_csv('koreanTitles2.csv', index=False, encoding='utf-8')
