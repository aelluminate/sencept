import logging
import pandas as pd
from tqdm import tqdm

from utils.generators.string import generate_string
from utils.generators.number import generate_number
from utils.generators.date import generate_date
from utils.generators.time import generate_time
from utils.generators.boolean import generate_boolean
from utils.generators.operations import perform_operation
from utils.generators.conditions import handle_condition


def generate_data_from_schema(schema, num_rows):
    data = []
    existing_users = {}

    logging.info("[INFO] GENERATING DATA")
    for _ in tqdm(range(num_rows), desc="Generating data", unit="record"):
        row = {}
        parent_values = {}

        for column, config in schema.items():
            condition_result = handle_condition(config, row)
            if condition_result is None:
                row[column] = None
                continue

            if config["type"] == "string":
                value = generate_string(config)
            elif config["type"] == "number":
                value = generate_number(config, row)
            elif config["type"] == "date":
                value = generate_date(config, row)
            elif config["type"] == "time":
                value = generate_time(config, row)
            elif config["type"] == "boolean":
                value = generate_boolean(config)
            else:
                value = None

            inputs = config.get("inputs")
            if inputs:
                input_values = [
                    row.get(field, parent_values.get(field)) for field in inputs
                ]
                if "operation" in config:
                    value = perform_operation(config, input_values)

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
    logging.info("[INFO] DATA GENERATION COMPLETE")
    return pd.DataFrame(data)
