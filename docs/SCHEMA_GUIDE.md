# Schema Guide

The schema is a JSON object that defines the structure and rules for generating synthetic data. Each key in the schema represents a column in the dataset, and its value is a configuration object that specifies how the data for that column should be generated.

## Schema Properties

### 1. "`type`"
- **Description**: Specifies the data type of the column.
- **Allowed Values**:
  - `"string"`: Generates text data.
  - `"number"`: Generates numeric data.
  - `"date"`: Generates date values.
  - `"time"`: Generates time values.
  - `"boolean"`: Generates boolean values (0 or 1).
- **Example**: 

    ```json
    "age": {
        "type": "number"
    }
    ```

### 2. "`value`"
- **Description**: Assigns a fixed value to the column. If specified, all other properties are ignored.
- **Allowed Values**: Any valid value based on the column type.
- **Example**: 

    ```json
    "country": {
        "type": "string",
        "value": "Philippines"
    }
    ```

### 3. "`choices`"
- **Description**: Specifies a list of possible values for the column. A random value is selected from this list.
- **Applicable Types**: `string`, `number`, `boolean`.
- **Example**:

    ```json
    "sex": {
        "type": "string",
        "choices": ["M", "F", "O"]
    }
    ```

### 4. "`weight`"
- **Description**: Specifies how random choices are weighted. If set to "random", weights are generated using a Dirichlet distribution.
- **Applicable Types**: `string`, `number`, `boolean` (when `choices` is used).
- **Example**:

    ```json
    "payment_method": {
        "type": "string",
        "choices": ["GCash", "Maya", "Credit Card"],
        "weight": "random"
    }
    ```