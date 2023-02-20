import pandas as pd

# Read the input CSV file into a pandas DataFrame
df = pd.read_csv('csv_files/final_dataset.csv')

# Remove duplicates and store unique rows in a new DataFrame
df_unique = df.drop_duplicates()

# Write the unique rows to a new CSV file
df_unique.to_csv('csv_files/unique_dataset.csv', index=False)
