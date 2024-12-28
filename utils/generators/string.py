import random
import numpy as np
from faker import Faker

fake = Faker("en_US")


def generate_string(config):
    if "choices" in config:
        if "weight" in config and config["weight"] == "random":
            weights = np.random.dirichlet(np.ones(len(config["choices"])), size=1)[0]
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
