import random
import numpy as np


from utils.randomizers.algorithms import (
    generate_exponential_weights,
    generate_power_law_weights,
    generate_beta_weights,
    generate_lognormal_weights,
    generate_zipf_weights,
)


def generate_boolean(config, row=None):
    choices = config.get("choices", [0, 1])

    if "weight" in config:
        weight_config = config["weight"]
        if weight_config.get("balanced", False):
            weights = np.ones(len(choices)) / len(choices)
        else:
            algorithm = weight_config.get("algorithm", "dirichlet")
            if algorithm == "exponential":
                weights = generate_exponential_weights(len(choices))
            elif algorithm == "power_law":
                weights = generate_power_law_weights(len(choices))
            elif algorithm == "beta":
                weights = generate_beta_weights(len(choices))
            elif algorithm == "lognormal":
                weights = generate_lognormal_weights(len(choices))
            elif algorithm == "zipf":
                weights = generate_zipf_weights(len(choices))
            else:
                weights = np.random.dirichlet(np.ones(len(choices)), size=1)[0]
        return np.random.choice(choices, p=weights)
    else:
        return random.choice(choices)
