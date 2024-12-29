from datetime import date, datetime


def perform_operation(config, input_values):
    if config["operation"] == "sum":
        return sum([v for v in input_values if v is not None])
    elif config["operation"] == "percentage":
        discount_percentage = input_values[0]
        total_purchase = input_values[1]
        if discount_percentage is not None and total_purchase is not None:
            return round((discount_percentage / 100) * total_purchase, 2)
        else:
            return None
    elif config["operation"] == "subtract":
        input_values = [v for v in input_values if v is not None]
        if len(input_values) == 2:
            value1, value2 = input_values
            if isinstance(value1, (date, datetime)) and isinstance(
                value2, (date, datetime)
            ):
                return (value1 - value2).days
            elif isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
                return round(value1 - value2, 2)
            else:
                return None
        else:
            return None
    return None
