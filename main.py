import os
import argparse
from datetime import datetime
from lib.synthetic import generate_synthetic_data
from lib.file_operations import save_to_csv, save_to_json, save_to_excel


def main():
    parser = argparse.ArgumentParser(
        description="Generate synthetic data based on a schema."
    )
    parser.add_argument(
        "--numrows", type=int, required=True, help="Number of rows to generate."
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["csv", "json", "xlsx"],
        default="csv",
        help="Output format for the generated data (default: csv).",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/generated/",
        help="Output directory for the generated file (default: data/generated/).",
    )

    args = parser.parse_args()

    synthetic_df = generate_synthetic_data(args.numrows)

    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"synthetic_data_{current_datetime}_{args.numrows}"

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    output_path = os.path.join(args.output, filename)
    if args.format == "csv":
        save_to_csv(synthetic_df, f"{output_path}.csv")
    elif args.format == "json":
        save_to_json(synthetic_df, f"{output_path}.json")
    elif args.format == "xlsx":
        save_to_excel(synthetic_df, f"{output_path}.xlsx")

    print(f"Data saved to {output_path}.{args.format}")


if __name__ == "__main__":
    main()
