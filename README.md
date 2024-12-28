# Sencept

![version](https://img.shields.io/badge/version-v0.2.1-black?style=for-the-badge&labelColor=%231f1f1e&color=%23f3f4f0)

**Sencept** is a *quite* powerful framework for generating high-quality synthetic data. The name blends "synthesis" and "concept," reflecting the project's focus on conceptualizing and synthesizing realistic datasets for training and evaluating machine learning models. With Sencept, you can create customizable, schema-driven synthetic data that mimics real-world scenarios, making it ideal for testing, development, and research.

## ✨ Features

- **Schema-Driven Data Generation**: Define your data structure using a JSON schema, and Sencept will generate synthetic data based on your specifications.
- **Flexible Field Types**: Supports various data types, including strings, numbers, dates, booleans, and more.
- **Conditional Logic**: Generate data based on conditions and dependencies between fields.
- **Unique Values**: Ensure unique values for specific fields like user_id or order_id.
- **CSV Export**: Save generated data to CSV files for easy integration with other tools.
- **Customizable**: Easily extend and adapt the framework to meet your specific needs.
- (🆕) **Weighted Random Choices**: Assign weights to choices for more realistic data distribution.
- (🆕) **Dynamic Operations**: Perform calculations like sums, percentages, and subtractions on generated data.

###### **Sencept** is still in active development, and new features are being added regularly. We also had a todo list that you can check out in the **[TODO](docs/TODO.md)** guide; these are the features that are planned to be implemented in the future.

## 🔨 Usage

### 1. Define Your Schema
Create a JSON schema file (e.g., `generate.json`) to define the structure of your synthetic data and place it in the 📂 `schemas` directory. Here's an example schema:

```json
{
    "user_id": {
        "type": "number",
        "unique": true,
        "format": {
            "prefix": "****"
        },
        "length": 6
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
    }
}
```

For more advanced features like conditional logic, dynamic operations, and dependencies, refer to the **[SCHEMA GUIDE](docs/SCHEMA_GUIDE.md)**.

### 2. Generate Synthetic Data

Run the main.py script to generate synthetic data based on your schema:

```bash
python -B -m main
```

The generated data will be saved as a CSV file *(by default)* in the 📂 `data/generated` directory. You can customize the output directory and file name in the `main.py` script but the default is `data/generated/synthetic_data_<timestamp>_<num_rows_to_generate>.csv`.
### 3. Customize Generation

You can customize the number of rows by modifying the main.py script:

```python
num_rows_to_generate = 5000  # Change this to generate more or fewer rows
```

This script will generate 5000 rows of synthetic data based on the schema you defined.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to Sencept, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request with a detailed description of your changes.

###### We'll be updating the **[CONTRIBUTING](CONTRIBUTING.md)** guide soon, so stay tuned!

## 📄 License

**Sencept** is released under the MIT License. See the [LICENSE](LICENSE) file for more information.

## 🌐 Contacts

- [@noeyislearning](https://www.linkedin.com/in/noeyislearning/) on LinkedIn

For questions, feedback, or support, please open an issue on the this repository or contact the maintainer directly.

## 🔥 Activity 

<img src="https://repobeats.axiom.co/api/embed/b13935418cfac1a18eb92baab7dc0a2663cda506.svg" alt="Repobeats analytics image" width="100%" />

<br />

<div align="center">
    <img src="https://img.shields.io/badge/Powered_by-Aelluminate-blue?style=for-the-badge&labelColor=%231f1f1e&color=%23f3f4f0" alt="Powered by Aelluminate">
</div>