import random
import numpy as np
from faker import Faker

fake = Faker("en_US")


def generate_string(config):
    if "choices" in config:
        if "weight" in config and config["weight"] == "random":
            weights = np.random.dirichlet(np.ones(len(config["choices"])), size=1)[0]
            return np.random.choice(config["choices"], p=weights)
        else:
            return random.choice(config["choices"])
    elif "value" in config:
        return config["value"]
    else:
        return fake.word()
