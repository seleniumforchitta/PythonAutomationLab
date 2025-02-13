import pandas as pd

# Target website - https://football-data.co.uk/englandm.php
df_premier24 = pd.read_csv('https://football-data.co.uk/mmz4281/2425/E0.csv'); # Put the CSV link address from the website 
print(df_premier24);
# renaming the column
df_premier24.rename(columns={
    'FTHG':'Home_Goals',
    'FTAG':'Away_Goals'
}, inplace=True)
#After renaming the columns
print(df_premier24);


