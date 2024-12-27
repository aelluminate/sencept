import random
import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime
from tqdm import tqdm
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

fake = Faker("en_US")


def generate_data_from_schema(schema, num_rows=1000):
    data = []
    existing_users = {}

    logging.info("Starting data generation")
    for _ in tqdm(range(num_rows), desc="Generating data", unit="record"):
        row = {}
        parent_values = {}

        for column, config in schema.items():
            condition = config.get("condition")
            if condition:
                condition_field = condition["field"]
                condition_value = condition.get("value")
                condition_values = condition.get("values")
                if (
                    condition_value is not None
                    and row.get(condition_field) != condition_value
                ):
                    row[column] = None
                    continue
                if (
                    condition_values is not None
                    and row.get(condition_field) not in condition_values
                ):
                    row[column] = None
                    continue

            if config["type"] == "string":
                if "choices" in config:
                    if "weight" in config and config["weight"] == "random":
                        weights = np.random.dirichlet(
                            np.ones(len(config["choices"])), size=1
                        )[0]
                        value = np.random.choice(config["choices"], p=weights)
                    else:
                        value = random.choice(config["choices"])
                elif "value" in config:
                    value = config["value"]
                else:
                    value = fake.word()
            elif config["type"] == "number":
                if "format" in config and "prefix" in config["format"]:
                    prefix = config["format"]["prefix"]
                    length = config.get("length", 6)
                    number = "".join([str(random.randint(0, 9)) for _ in range(length)])
                    value = f"{prefix}{number}"
                elif "range" in config:
                    value = random.randint(
                        config["range"]["min"], config["range"]["max"]
                    )
                elif "choices" in config:
                    if "weight" in config and config["weight"] == "random":
                        weights = np.random.dirichlet(
                            np.ones(len(config["choices"])), size=1
                        )[0]
                        value = np.random.choice(config["choices"], p=weights)
                    else:
                        value = random.choice(config["choices"])
                elif "mapping" in config:
                    mapping_field = config["mapping"]["field"]
                    mapping_values = config["mapping"]["values"]
                    if row.get(mapping_field) is not None:
                        lookup_key = str(int(row[mapping_field]))
                        value = mapping_values.get(lookup_key)
                    else:
                        value = None
                else:
                    value = random.randint(0, 100)
            elif config["type"] == "date":
                start_date = config.get("dates", {}).get("min", "2000-01-01")
                end_date = config.get("dates", {}).get("max", "today")

                if end_date == "today":
                    end_date = datetime.today().strftime("%Y-%m-%d")

                try:
                    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                except ValueError as e:
                    raise ValueError(
                        f"Invalid date format in schema for column {column}: {e}"
                    )

                value = fake.date_between(start_date=start_date, end_date=end_date)
            elif config["type"] == "boolean":
                value = random.choice(config.get("choices", [0, 1]))

            inputs = config.get("inputs")
            if inputs:
                input_values = []
                for input_field in inputs:
                    input_value = row.get(input_field)
                    if input_value is None:
                        input_value = parent_values.get(input_field)
                    input_values.append(input_value)

                if "operation" in config:
                    if config["operation"] == "sum":
                        value = sum([v for v in input_values if v is not None])
                    elif config["operation"] == "percentage":
                        discount_percentage = input_values[0]
                        total_purchase = input_values[1]
                        if (
                            discount_percentage is not None
                            and total_purchase is not None
                        ):
                            value = (discount_percentage / 100) * total_purchase
                            value = round(value, 2)
                        else:
                            value = None
                    elif config["operation"] == "subtract":
                        # Calculate total purchase after discount
                        total_purchase = input_values[0]
                        total_discount = input_values[1]
                        if total_purchase is not None and total_discount is not None:
                            value = total_purchase - total_discount
                            value = round(value, 2)
                        else:
                            value = None

            parent = config.get("parent")
            if parent:
                parent_value = row.get(parent)
                if parent_value is None:
                    parent_value = parent_values.get(parent)
                if (
                    parent_value in existing_users
                    and column in existing_users[parent_value]
                ):
                    value = existing_users[parent_value][column]
                else:
                    if parent_value not in existing_users:
                        existing_users[parent_value] = {}
                    existing_users[parent_value][column] = value
                parent_values[parent] = parent_value

            row[column] = value

        for column in schema.keys():
            if column not in row:
                row[column] = None

        data.append(row)
    logging.info("Data generation complete")
    return pd.DataFrame(data)
