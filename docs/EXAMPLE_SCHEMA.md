# Example Schema

Here’s an example schema that uses multiple properties:

```json
{
    "user_id": {
        "type": "number",
        "unique": true,
        "format": {
            "prefix": "****",
            "length": 6
        }
    },
    "age": {
        "type": "number",
        "range": {
            "min": 18,
            "max": 60
        }
    },
    "payment_method": {
        "type": "string",
        "choices": ["GCash", "Maya", "Credit Card"],
        "weight": "random"
    },
    "total_purchase": {
        "type": "number",
        "range": {
            "min": 50,
            "max": 9999
        }
    },
    "total_discount": {
        "type": "number",
        "inputs": ["total_discount_percentage", "total_purchase"],
        "operation": "percentage"
    }
}
```