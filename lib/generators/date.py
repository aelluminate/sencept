from datetime import datetime, timedelta, date
from faker import Faker
import random

fake = Faker("en_US")


def generate_date(config, row):
    if "dependency" in config:
        dependencies = config["dependency"]
        for dependency in dependencies:
            dependency_field = dependency["field"]
            offset_min = dependency["offset"]["min"]
            offset_max = dependency["offset"].get("max")
            if row.get(dependency_field) is not None:
                base_date = row[dependency_field]
                if offset_max is None:
                    today = datetime.today().date()
                    offset_max = (today - base_date).days
                random_offset = random.randint(offset_min, offset_max)
                return base_date + timedelta(days=random_offset)
        return None
    elif "value" in config:
        return config["value"]
    else:
        start_date = config.get("dates", {}).get("min", "2000-01-01")
        end_date = config.get("dates", {}).get("max", "today")

        if end_date == "today":
            end_date = datetime.today().strftime("%Y-%m-%d")

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Invalid date format in schema for column: {e}")

        return fake.date_between(start_date=start_date, end_date=end_date)
