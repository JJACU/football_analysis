import pandas as pd
import re

df = pd.read_csv('C:\pythonML\events.csv')



# Filtracja danych
goal_df = df[df['text'].str.contains(r'Goal')]
new_df = goal_df.query('bodypart == 1.0 & location == 3.0')

# Wyświetlenie wyniku
print(new_df[['text', 'event_type', 'event_team', 'player', 'player2', 'location', 'bodypart', 'assist_method']].head(10))

