import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

WB_TOKEN = os.getenv("WB_API_TOKEN")
MPSTATS_KEY = os.getenv("MPSTATS_API_KEY")
SPREADSHEET_ID = os.getenv("GOOGLE_SPREADSHEET_ID")
SHEET_NAME = os.getenv("GOOGLE_WORKSHEET_NAME", "Sales")

def main():
    # сюда позже прикрутим WB/MPStats + запись в Google Sheets
    df = pd.DataFrame([{"date": "2025-08-13", "orders": 0, "revenue": 0}])
    print(df)

if __name__ == "__main__":
    main()
