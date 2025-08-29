"""
clean_columns.py
Removes unnecessary columns from the dataset.
"""

import pandas as pd

def clean_columns(input_path="data/Real estate.csv", output_path="data/cleaned_data.csv"):
    # Load dataset
    df = pd.read_csv(input_path)

    # Example: Drop transaction date if not required
    if 'transaction_date' in df.columns:
        df.drop(columns=['transaction_date'], inplace=True)

    # Save cleaned dataset
    df.to_csv(output_path, index=False)
    print(f"Columns cleaned and saved to {output_path}")

if __name__ == "__main__":
    clean_columns()
