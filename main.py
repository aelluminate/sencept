import os
from lib.data_generator import generate_synthetic_data
from lib.file_operations import save_to_csv
from datetime import datetime

if __name__ == "__main__":
    # Change this number to generate rows
    num_rows_to_generate = 523523
    month = 2
    year = 2024

    # Generate synthetic data
    synthetic_df = generate_synthetic_data(num_rows_to_generate, month=month, year=year)

    # Create a filename with the current datetime
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = "data"
    output_path = f"{output_dir}/synthetic_data_{current_datetime}_m{month}y{year}_{num_rows_to_generate}.csv"

    # Create the directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the generated data to the file
    save_to_csv(synthetic_df, output_path)
