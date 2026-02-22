import pandas as pd
import re
df = pd.read_csv('this.csv')
def remove_noise(text):
    if pd.isna(text): return text
    text = re.sub(r'\[.*?\]', '', str(text)) # Removes anything in brackets
    return text.replace('†', '').replace('‡', '').strip()
def to_numeric(value):
    if pd.isna(value): return 0
    clean_val = re.sub(r'[^\d.]', '', str(value)) # Keeps only digits and dots
    return float(clean_val) if clean_val else 0
df['Artist'] = df['Artist'].apply(remove_noise)
df['Tour_Title'] = df['Tour title'].apply(remove_noise)
df['Actual_Gross'] = df['Actual\xa0gross'].apply(to_numeric)
df['Start_Year'] = df['Year(s)'].astype(str).str[:4] # Extracts '2023' from '2023-2024'
structured_df = df[[
    'Rank', 'Artist', 'Tour_Title', 'Start_Year', 'Shows', 'Actual_Gross'
]].rename(columns={'Shows': 'Total_Shows', 'Actual_Gross': 'Revenue_USD'})
structured_df.to_csv('cleaned_tour_data.csv', index=False)
print("Data Successfully Organized!")
