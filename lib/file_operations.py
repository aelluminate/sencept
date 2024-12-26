def save_to_csv(df, filename="synthetic_data.csv"):
    """Saves the DataFrame to a CSV file."""
    try:
        df.to_csv(
            filename, index=False, encoding="utf-8"
        )  # Important for special characters
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")
