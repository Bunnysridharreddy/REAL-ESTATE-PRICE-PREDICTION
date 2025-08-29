"""
encode_categorical.py
Encodes categorical features (if present).
"""

import pandas as pd

def encode_categorical(input_path="data/cleaned_data.csv", output_path="data/cleaned_data.csv"):
    df = pd.read_csv(input_path)

    # Example: One-hot encode a 'location' column (if exists)
    if 'location' in df.columns:
        df = pd.get_dummies(df, columns=['location'], drop_first=True)

    df.to_csv(output_path, index=False)
    print(f"Categorical encoding done and saved to {output_path}")

if __name__ == "__main__":
    encode_categorical()
