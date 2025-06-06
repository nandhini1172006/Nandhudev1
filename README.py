import pandas as pd

# Load the dataset
df = pd.read_csv('customer_personality_analysis.csv')

# Handle missing values
df.fillna(df.mean(), inplace=True)  # Fill numerical columns with mean
df.fillna(df.mode().iloc[0], inplace=True)  # Fill categorical columns with mode

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize text values
df['Education'] = df['Education'].str.lower()
df['Marital_Status'] = df['Marital_Status'].str.lower()

# Convert date formats
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%Y-%m-%d')

# Rename column headers
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Check and fix data types
df['year_birth'] = df['year_birth'].astype(int)
df['income'] = df['income'].astype(float)

# Save the cleaned dataset
df.to_csv('cleaned_customer_personality_analysis.csv', index=False)
