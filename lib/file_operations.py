def save_to_csv(df, filename):
    try:
        df.to_csv(filename, index=False, encoding="utf-8")
    except Exception as e:
        print(f"Error saving to CSV: {e}")


def save_to_json(df, filename):
    try:
        date_columns = df.select_dtypes(include=["datetime64"]).columns
        for col in date_columns:
            df[col] = df[col].dt.strftime("%Y-%m-%d")

        df.to_json(filename, orient="records", lines=True, date_format="iso")
    except Exception as e:
        print(f"Error saving to JSON: {e}")


def save_to_excel(df, filename):
    try:
        df.to_excel(filename, index=False)
    except Exception as e:
        print(f"Error saving to Excel: {e}")
