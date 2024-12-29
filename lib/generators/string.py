import random
import numpy as np
from faker import Faker

from utils.randomizers.algorithms import (
    generate_exponential_weights,
    generate_power_law_weights,
    generate_beta_weights,
    generate_lognormal_weights,
    generate_zipf_weights,
)

fake = Faker("en_US")


def generate_string(config):
    if "choices" in config:
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
            value = np.random.choice(config["choices"], p=weights)
        else:
            value = random.choice(config["choices"])
    elif "value" in config:
        value = config["value"]
    else:
        value = fake.word()

    case = config.get("case", "mixed")
    if case == "uppercase":
        value = value.upper()
    elif case == "lowercase":
        value = value.lower()

    return value
