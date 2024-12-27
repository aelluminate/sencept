from utils.load_schema import load_schema
from utils.generators.schema import generate_data_from_schema


def generate_synthetic_data(num_rows, schema_file="generate.json"):
    schema = load_schema(schema_file)
    if schema is None:
        raise ValueError(f"Failed to load schema file {schema_file}")

    df = generate_data_from_schema(schema, num_rows)
    return df
