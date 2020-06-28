import pandas as pd
df1 = pd.read_csv("koreanTitles.csv")
df2 = pd.read_csv("koreanTitles2.csv")
dx = pd.merge(df1,df2, on='Title', how='outer')
dx['Korean title']=dx['Korean title_x'].combine_first(dx['Korean title_y'])
dx = dx.drop(['Korean title_x', 'Korean title_y'],1)
dx.to_csv('koreanTitles.csv', index=False, encoding='utf-8')
