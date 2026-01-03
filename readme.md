# Insurance Claims ETL Pipeline

A mini **Insurance Claims ETL Project** demonstrating a full **Extract → Transform → Load (ETL)** workflow using Python and CSV files.  

This project simulates a real-world data engineering pipeline for insurance claim data.

---

## Project Structure
NITHYA GIT/
├── data/
│ ├── raw/ # Original raw CSV data
│ │ └── insurance_claims.csv
│ ├── processed/ # Cleaned and final tables
│ │ ├── insurance_claims_clean.csv
│ │ └── final_tables/
│ │ ├── fact_claims.csv
│ │ └── dim_claim_type.csv
├── src/ # Python scripts
│ ├── extract.py # Extracts raw CSV into Python
│ ├── transform.py # Cleans data (nulls, negatives)
│ └── load.py # Creates fact and dimension tables
├── tests/ # (Optional: future test scripts)
├── sql/ # (Optional: create SQL tables)
└── README.md


---

## ETL Steps

### 1️⃣ Extract
- Reads raw CSV (`insurance_claims.csv`) into a Pandas DataFrame.
- Prints row and column info for validation.

### 2️⃣ Transform
- Removes rows with **null** `claim_amount`.
- Removes rows with **negative** `claim_amount`.
- Saves cleaned CSV to `data/processed/insurance_claims_clean.csv`.

### 3️⃣ Load
- Splits cleaned data into:
  - **Fact table:** `fact_claims.csv` (claim info)
  - **Dimension table:** `dim_claim_type.csv` (claim types)
- Saves tables to `data/processed/final_tables/`

---

## Sample Data

**Raw Data:**
| claim_id | policy_id | customer_id | claim_date | claim_amount | claim_status | claim_type |
|----------|-----------|-------------|------------|--------------|--------------|------------|
| 1001     | P10001    | C501        | 2024-01-05 | 25000        | Approved     | Health     |
| 1002     | P10002    | C502        | 2024-01-08 | 0            | Rejected     | Vehicle    |
| 1003     | P10003    | C503        | 2024-01-10 | 18000        | Approved     | Life       |
| 1004     | P10004    | C504        | 2024-01-12 | (null)       | Pending      | Health     |
| 1005     | P10005    | C505        | 2024-01-15 | 42000        | Approved     | Vehicle    |
| 1006     | P10006    | C506        | 2024-01-18 | -500         | Rejected     | Health     |

---

## Technologies Used
- **Python 3.12**
- **Pandas**
- Git (version control)
- CSV files for raw and processed data

---

## How to Run

1. **Clone the repository**
```bash
git clone <your-repo-link>
cd Nithya\ Git


Install dependencies

python -m pip install pandas


Run ETL steps

python src/extract.py
python src/transform.py
python src/load.py


Check processed tables

Cleaned data: data/processed/insurance_claims_clean.csv

Fact & dimension tables: data/processed/final_tables/

Outcome / Takeaways

Built a full ETL pipeline from scratch

Learned Extract → Transform → Load using Python

Gained hands-on experience with insurance data

Can demonstrate a professional mini project in interviews

Future Enhancements

Load data into SQL database

Add unit tests for each step

Handle more complex business rules

Automate daily ingestion using Airflow


---

## STEP 3: Save + commit

```bash
git add README.md
git commit -m "Add professional README for insurance ETL project"


