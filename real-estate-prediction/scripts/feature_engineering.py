"""
feature_engineering.py
Adds new features like transaction year.
"""

import pandas as pd

def add_features(input_path="data/cleaned_data.csv", output_path="data/cleaned_data_with_transaction_year.csv"):
    df = pd.read_csv(input_path)

    # Extract year from 'transaction_date' if present
    if 'transaction_date' in df.columns:
        df['transaction_year'] = df['transaction_date'].astype(str).str.extract(r'(\d{4})').astype(int)

    df.to_csv(output_path, index=False)
    print(f"Feature engineering done and saved to {output_path}")

if __name__ == "__main__":
    add_features()
