import pandas as pd
import re

df = pd.read_csv('C:\pythonML\events.csv')

goal_df = df[df['text'].str.contains(r'Goal!') & df['assist_method'] != 0]
print(goal_df.tail())