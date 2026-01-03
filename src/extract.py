import pandas as pd

def extract_data(path):
    df = pd.read_csv(path)
    print("Rows:", df.shape[0])
    print("Columns:", df.columns.tolist())
    return df

if __name__ == "__main__":
    extract_data("data/raw/insurance_claims.csv")
