import pandas as pd
import re

df = pd.read_csv('C:\pythonML\events.csv')

new_df = df[df['text'].str.contains(r'Goal', case=False, na=False )]


goal_counts = new_df['player'].value_counts()

top_player =  goal_counts.idxmax()
top_count = goal_counts.max()

print(f'Graczem z największą iloscia goli jest {top_player} z iloscia goli {top_count}')