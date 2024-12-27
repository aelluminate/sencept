import random
import logging
import pandas as pd
import numpy as np
from faker import Faker
from tqdm import tqdm
from datetime import timedelta, datetime
import json

fake = Faker("en_US")


# Load JSON schema
def load_schema(schema_file="data_schema.json"):
    with open(schema_file, "r") as f:
        return json.load(f)


# Generate data based on schema
def generate_data_from_schema(schema, num_rows=1000):
    data = []
    for _ in range(num_rows):
        row = {}
        for column, config in schema.items():
            if config["type"] == "string":
                if "format" in config:
                    if "random_int" in config["format"]:
                        start, end = map(
                            int,
                            config["format"]
                            .split("{random_int:")[1]
                            .split("}")[0]
                            .split(","),
                        )
                        row[column] = config["format"].replace(
                            "{random_int:" + f"{start},{end}" + "}",
                            str(random.randint(start, end)),
                        )
                elif "choices" in config:
                    weights = config.get("weights", None)
                    row[column] = random.choices(
                        config["choices"], weights=weights, k=1
                    )[0]
                else:
                    row[column] = fake.word()
            elif config["type"] == "number":
                row[column] = random.randint(
                    config.get("min", 0), config.get("max", 100)
                )
            elif config["type"] == "date":
                row[column] = fake.date_between(
                    start_date=config.get("start_date", "-5y"),
                    end_date=config.get("end_date", "today"),
                )
        data.append(row)
    return pd.DataFrame(data)


# Main function
def generate_synthetic_data(
    num_rows=1000, month=None, year=None, schema_file="data_schema.json"
):
    schema = load_schema(schema_file)
    df = generate_data_from_schema(schema, num_rows)
    return df
