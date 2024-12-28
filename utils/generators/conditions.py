def handle_condition(config, row):
    condition = config.get("condition")
    if condition:
        condition_field = condition["field"]
        condition_value = condition.get("value")
        condition_values = condition.get("values")
        if condition_value is not None and row.get(condition_field) != condition_value:
            return None
        if (
            condition_values is not None
            and row.get(condition_field) not in condition_values
        ):
            return None
    return "continue"
