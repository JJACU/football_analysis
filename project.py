import pandas as pd
import re

df = pd.read_csv('C:\pythonML\events.csv')

new_df = df[df['text'].str.contains(r'Goal', case=False, na=False )]
print(new_df.count())