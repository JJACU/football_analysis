import pandas as pd
import re

df = pd.read_csv('C:\pythonML\events.csv')
new_df = df[(df['event_type'] == 6) & (df['time'].between(1,10))]

print(new_df[['time', 'text', 'event_type', 'event_team', 'opponent', 'player']])