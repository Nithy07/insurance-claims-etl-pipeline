import pandas as pd

def transform_data(input_path, output_path):
    # 1️⃣ Read the raw CSV
    df = pd.read_csv(input_path)

    # 2️⃣ Remove rows where claim_amount is null
    df = df[df['claim_amount'].notnull()]

    # 3️⃣ Remove rows where claim_amount is negative
    df = df[df['claim_amount'] >= 0]

    # 4️⃣ Optional: reset index
    df = df.reset_index(drop=True)

    # 5️⃣ Save the cleaned data to processed folder
    df.to_csv(output_path, index=False)
    print(f"Data transformed and saved: {output_path}")
    print("Rows:", df.shape[0])
    print("Columns:", df.columns.tolist())

if __name__ == "__main__":
    transform_data("data/raw/insurance_claims.csv",
                   "data/processed/insurance_claims_clean.csv")
