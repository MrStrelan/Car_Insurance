from pathlib import Path
import sys
import pandas as pd

def load_claims_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    try:
        # low_memory=False helps avoid dtype inference warnings on large files
        df = pd.read_csv(path, low_memory=False)
    except Exception as e:
        print(f"ERROR reading CSV: {e}", file=sys.stderr)
        sys.exit(1)
    return df

def main():
    project_root = Path(__file__).resolve().parent
    csv_path = project_root / "data" / "claims_train.csv"

    df = load_claims_csv(csv_path)

    print(f"Loaded: {csv_path}")
    print(f"Shape: {df.shape}")
    print("Columns and dtypes:")
    print(df.dtypes)
    print("\nFirst 5 rows:")
    print(df.head())
    print("distinct IDpolicy values:", df["IDpol"].nunique())
if __name__ == "__main__":
    main()
