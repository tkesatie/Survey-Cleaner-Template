import pandas as pd
data = {
    'respondent_id': [1, 2, 3],
    'zip_code': ['87102', '90210', '10001'],
    'entry_date': ['2023-01-01', '2023-01-15', '2023-05-20']
}
df = pd.DataFrame(data)

#Client wants the date in the format of YYYYMMDD
df['entry_date'] = df['entry_date'].str.replace('-', '')
df['zip_code'] = pd.to_numeric(df['zip_code'], errors='coerce')

# Example map of zip codes to regions (this would be more complex in a real scenario). This doesn't match actual zip code regions.
df['region'] = df['zip_code'].map(lambda x: 'East' if (10000 <= x < 20000) else ('West' if (80000 <= x < 100000) else ('South' if (30000 <= x < 80000) else 'Unknown')))

print(df.head())
print(df.info())