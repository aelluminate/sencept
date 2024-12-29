import json
import os


def load_schema(schema_file):
    schema_path = os.path.join("schemas", schema_file)

    if not os.path.exists(schema_path):
        print(f"Schema file '{schema_path}' not found.")
        return None

    try:
        with open(schema_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON schema file '{schema_path}': {e}")
        return None
