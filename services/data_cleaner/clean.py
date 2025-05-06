import sys
import pandas as pd
from io import StringIO

def clean_dataset(csv_string):
    try:
        # Replace literal \n with real newlines
        csv_string = csv_string.replace('\\n', '\n')
        df = pd.read_csv(StringIO(csv_string), on_bad_lines='skip')
        df_cleaned = df.dropna()
        return df_cleaned.to_csv(index=False)
    except Exception as e:
        return f"Error cleaning dataset: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean.py '<csv_string>'")
        sys.exit(1)
    csv_string = sys.argv[1]
    result = clean_dataset(csv_string)
    print(result)
