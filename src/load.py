import pandas as pd
import os

def load_data(input_path, output_folder):
    # Read cleaned data
    df = pd.read_csv(input_path)

    # Split into tables (simulate dimensional modeling)
    # Fact table: claims
    fact_claims = df[['claim_id', 'policy_id', 'customer_id', 'claim_date', 'claim_amount', 'claim_status']]

    # Dimension table: claim_type
    dim_claim_type = df[['claim_id', 'claim_type']]

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Save fact and dimension tables
    fact_claims.to_csv(os.path.join(output_folder, "fact_claims.csv"), index=False)
    dim_claim_type.to_csv(os.path.join(output_folder, "dim_claim_type.csv"), index=False)

    print(f"Fact and dimension tables created in {output_folder}")
    print("Fact table rows:", fact_claims.shape[0])
    print("Dim table rows:", dim_claim_type.shape[0])

if __name__ == "__main__":
    load_data("data/processed/insurance_claims_clean.csv", "data/processed/final_tables")
