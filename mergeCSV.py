import pandas as pd
df1 = pd.read_csv("koreanTitles.csv")
df2 = pd.read_csv("koreanTitles2.csv")
dx = pd.merge(df1,df2, how='outer')
print(dx)
dx.to_csv('koreanTitles.csv', index=False, encoding='utf-8')