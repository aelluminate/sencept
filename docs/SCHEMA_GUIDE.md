# Schema Guide

![version](https://img.shields.io/badge/version-v0.2.1-black?style=for-the-badge&labelColor=%231f1f1e&color=%23f3f4f0)

The schema is a JSON object that defines the structure and rules for generating synthetic data. Each key in the schema represents a column in the dataset, and its value is a configuration object that specifies how the data for that column should be generated.

###### For example schema(s), refer to the **[EXAMPLE SCHEMA](EXAMPLE_SCHEMA.md)** guide.

## Types

- "`string`": Generates text data.
- "`number`": Generates numeric data.
- "`date`": Generates date values.
- "`time`": Generates time values.
- "`boolean`": Generates boolean values (0 or 1).


## Properties

### 1. "`type`"
Specifies the data type of the column.  

**Allowed Values**: `string`, `number`, `date`, `time`, `boolean`.

**Example**:
```json
"age": {
    "type": "number"
}
```

### 2. "`value`"
Assigns a fixed value to the column. If specified, all other properties are ignored.

**Allowed Values**: All

**Example**:
```json
"country": {
    "type": "string",
    "value": "Philippines"
}
```
### 3. "`choices`"
Specifies a list of possible values for the column. A random value is selected from this list.

**Applicable Types**: `string`, `number`, `boolean`.

**Example**:
```json
"sex": {
    "type": "string",
    "choices": ["M", "F", "O"]
}
```

### 4. "`weight`"
Specifies how random choices are weighted. If set to "random", weights are generated using a Dirichlet distribution.

**Applicable Types**: `string`, `number`, `boolean` (when choices is used).

**Example**:
```json
"payment_method": {
    "type": "string",
    "choices": ["GCash", "Maya", "Credit Card"],
    "weight": "random"
}
```

### 5. "`range`"
Specifies a range of numeric values. A random number is generated within this range.

**Applicable Types**: `number`.

**Properties**:
- `min`: The minimum value.
- `max`: The maximum value.

**Example**:
```json
"age": {
    "type": "number",
    "range": {
        "min": 18,
        "max": 60
    }
}
```

### 6. "`format`"

Specifies a custom format for generating values.

**Applicable Types**: `string`, `number`.

**Properties**:
- `prefix`: A prefix to prepend to the generated value.
- `length`: The length of the generated value (excluding the prefix).

**Example**:
```json
"user_id": {
    "type": "number",
    "format": {
        "prefix": "****",
        "length": 6
    }
}
```

### 7. "`dates`"
Specifies a date range for generating date values.

**Applicable Types**: `date`.

**Properties**:
- `min`: The minimum date (format: YYYY-MM-DD).
- `max`: The maximum date (format: YYYY-MM-DD or "today").

**Example**:
```json
"joined_date": {
    "type": "date",
    "dates": {
        "min": "2024-01-01",
        "max": "today"
    }
}
```

### 8. "`dependency`"
Specifies that the value of this column depends on another column.

**Applicable Types**: `date`, `time`.

**Properties**:
- `field`: The column this field depends on.
- `offset`: A range of days or time to add/subtract from the dependent field.

**Example**:
```json
"released_date": {
    "type": "date",
    "dependency": {
        "field": "purchased_date",
        "offset": {
            "min": 1,
            "max": 7
        }
    }
}
```

### 9. "`mapping`"
Maps the value of this column to another column's value using a dictionary.

**Applicable Types**: `number`.

**Properties**:
- `field`: The column to map from.
- `values`: A dictionary of key-value pairs for mapping.

**Example**:
```json
"tier_discount_percentage": {
    "type": "number",
    "mapping": {
        "field": "loyalty_tier",
        "values": {
            "1": 3,
            "2": 5,
            "3": 7,
            "4": 10
        }
    }
}
```

### 10. "`condition`"
Specifies a condition for generating the value of this column.

**Properties**:
- `field`: The column to check the condition against.
- `value`: The value the field must match.
- `values`: A list of values the field must match.

**Example**:
```json
"loyalty_tier": {
    "type": "string",
    "choices": [1, 2, 3, 4],
    "condition": {
        "field": "loyalty_program_member",
        "value": 1
    }
}
```

### 11. "`inputs`"
Specifies a list of columns whose values are used as inputs for an operation.

- **Applicable Types**: `number`.

**Example**:
```json
"total_discount": {
    "type": "number",
    "inputs": ["total_discount_percentage", "total_purchase"],
    "operation": "percentage"
}
```

### 12. "`operation`"
Specifies an operation to perform on the input values.

**Applicable Types**: `number`.

**Allowed Values**:
- "`sum`": Sums the input values.
- "`subtract`": Subtracts the second input value from the first.
- "`percentage`": Calculates a percentage of the input values.

**Example**:
```json
"total_purchase_after_discount": {
    "type": "number",
    "inputs": ["total_purchase", "total_discount"],
    "operation": "subtract"
}
```

### 13. "`parent`"
Specifies that the value of this column is tied to another column (e.g., for consistency across rows).

**Example**:
```json
"age": {
    "type": "number",
    "parent": "user_id"
}
```

### 14. "`unique`"
Ensures that the values in this column are unique.

**Applicable Types**: `string`, `number`.

Example:
```json
"user_id": {
    "type": "number",
    "unique": true
}
```