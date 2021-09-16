import pandas as pd

df = pd.DataFrame({'Song' : [], 'Score' : []})

df.to_excel('results.xlsx', index = False)