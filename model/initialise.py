import pandas as pd

df_input = pd.DataFrame({'Song' : [], 'Score' : []})

df_input.to_excel('results.xlsx', index = False)

df_output = pd.DataFrame({'Title' : [], 'Artist' : [], 'Lyrics' : []})

df_output.to_excel('results.xlsx', index = False)