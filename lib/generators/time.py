from datetime import time
import random


def generate_time(config, row):
    if "dependency" in config:
        dependency_field = config["dependency"]["field"]
        if row.get(dependency_field) is not None:
            return row[dependency_field]
        else:
            return None
    else:
        return time(
            hour=random.randint(0, 23),
            minute=random.randint(0, 59),
            second=random.randint(0, 59),
        ).strftime("%H:%M:%S")
