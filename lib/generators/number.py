import random
import numpy as np
import string


from utils.randomizers.algorithms import (
    generate_exponential_weights,
    generate_power_law_weights,
    generate_beta_weights,
    generate_lognormal_weights,
    generate_zipf_weights,
)


def generate_number(config, row):
    if "value" in config:
        return config["value"]
    if "format" in config:
        prefix = config["format"].get("prefix", "")
        suffix = config["format"].get("suffix", "")
        length = config.get("length", 6)
        if config.get("alphanumeric", False):
            characters = string.ascii_letters + string.digits
            random_part = "".join(random.choices(characters, k=length))
            case = config.get("case", "mixed")
            if case == "uppercase":
                random_part = random_part.upper()
            elif case == "lowercase":
                random_part = random_part.lower()
        else:
            random_part = "".join([str(random.randint(0, 9)) for _ in range(length)])
        return f"{prefix}{random_part}{suffix}"
    elif "range" in config:
        return random.randint(config["range"]["min"], config["range"]["max"])
    elif "choices" in config:
        if "weight" in config:
            weight_config = config["weight"]
            if weight_config.get("balanced", False):
                weights = np.ones(len(config["choices"])) / len(config["choices"])
            else:
                algorithm = weight_config.get("algorithm", "dirichlet")
                if algorithm == "exponential":
                    weights = generate_exponential_weights(len(config["choices"]))
                elif algorithm == "power_law":
                    weights = generate_power_law_weights(len(config["choices"]))
                elif algorithm == "beta":
                    weights = generate_beta_weights(len(config["choices"]))
                elif algorithm == "lognormal":
                    weights = generate_lognormal_weights(len(config["choices"]))
                elif algorithm == "zipf":
                    weights = generate_zipf_weights(len(config["choices"]))
                else:
                    weights = np.random.dirichlet(
                        np.ones(len(config["choices"])), size=1
                    )[0]
            return np.random.choice(config["choices"], p=weights)
        else:
            return random.choice(config["choices"])
    elif "mapping" in config:
        mapping_field = config["mapping"]["field"]
        mapping_values = config["mapping"]["values"]
        if row.get(mapping_field) is not None:
            lookup_key = str(int(row[mapping_field]))
            return mapping_values.get(lookup_key)
        else:
            return None
    else:
        return random.randint(0, 100)
