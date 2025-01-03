# Sencept CLI

![version](https://img.shields.io/badge/version-v0.2.6-black?style=for-the-badge&labelColor=%231f1f1e&color=%23f3f4f0) 
![powered-by](https://img.shields.io/badge/Powered_by-Aelluminate-blue?style=for-the-badge&labelColor=%231f1f1e&color=%23f3f4f0)

**Sencept** is a *not done yet* powerful command-line interface (CLI) tool designed to generate high-quality synthetic data. The name, a portmanteau of "synthesis" and "concept," reflects the project's core focus on conceptualizing and synthesizing realistic datasets for training and evaluating machine learning models. Sencept enables the creation of customizable, schema-driven synthetic data that accurately simulates real-world scenarios, making it an invaluable asset for testing, development, and research in machine learning.

## ✨ Features

- **Schema-Driven Data Generation**: Define your data structure using a JSON schema, and Sencept will generate synthetic data based on your specifications.
- **Flexible Field Types**: Supports various data types, including strings, numbers, dates, booleans, and more.
- **Conditional Logic**: Generate data based on conditions and dependencies between fields.
- **Unique Values**: Ensure unique values for specific fields like user_id or order_id.
- **CSV Export**: Save generated data to CSV files for easy integration with other tools.
- **Customizable**: Easily extend and adapt the framework to meet your specific needs.
- (🆕) **Weighted Random Choices**: Assign weights to choices for more realistic data distribution.
- (🆕) **Dynamic Operations**: Perform calculations like sums, percentages, and subtractions on generated data.
- (🆕) **Multiple Output Formats**: Save generated data in **CSV**, **JSON**, or **Excel** formats.
- (🆕) **Command-Line Interface (CLI)**: Easily generate data with customizable options via the command line.

###### **Sencept** is still in active development, and new features are being added regularly. We also had a todo list that you can check out in the **[TODO](docs/TODO.md)** guide; these are the features that are planned to be implemented in the future.

## 🔨 Usage

### 1. Define Your Schema
Create a JSON schema file (e.g., `generate.json`) to define the structure of your synthetic data and place it in the 📂 `schemas` directory. Here's an example schema:

```json
{
    "user_id": {
        "type": "number",
        "format": [
            {
                "position": "prefix",
                "contains": "63**",
                "count": 1
            },
            {
                "position": "suffix",
                "contains": "**",
                "count": 1
            }
        ],
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
        "weight": {
            "balanced": false,
            "algorithm": "beta"
        }
    }
}
```

For more advanced features like conditional logic, dynamic operations, and dependencies, refer to the **[SCHEMA GUIDE](docs/SCHEMA_GUIDE.md)** and for example schemas, check the **[EXAMPLES](docs/EXAMPLES.md)** guide.

### 2. Generate Synthetic Data (CLI)

Use the Command-Line Interface (CLI) to generate synthetic data with customizable options:

```bash
python main.py --numrows 1000 --format csv
```

**CLI Options**:

| Options | Description | Default | Required |
| --- | --- | --- | --- |
| `--numrows` | Number of rows to generate. | 1000 | Definitely **Yes** | 
| `--format` | Output format (csv, json, excel). | csv | **No** |
| `--output` | Output directory for the generated file. | `data/generated` | **No** |

**Example**:

- To generate 1000 rows, save as CSV, and change its output directory:
```bash
python main.py --numrows 1000 --format csv --output generated/sales
```

❗ NOTE: This will create a new directory named 📂 `generated/sales/` in the root folder.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to Sencept, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request with a detailed description of your changes.

###### We'll be updating the **[CONTRIBUTING](CONTRIBUTING.md)** guide soon, so stay tuned!

## 📄 License

**Sencept** is released under the MIT License. See the **[LICENSE](LICENSE)** file for more information.

## 🌐 Contacts

- **[@noeyislearning](https://www.linkedin.com/in/noeyislearning/)** on LinkedIn

For questions, feedback, or support, please open an issue on the this repository or contact the maintainer directly.

## 🔥 Activity 

<img src="https://repobeats.axiom.co/api/embed/b13935418cfac1a18eb92baab7dc0a2663cda506.svg" alt="Repobeats analytics image" width="100%" />

<br />

<div align="center">
    
###### To God be the glory.
</div>
