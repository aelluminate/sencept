import random


def generate_boolean(config):
    return random.choice(config.get("choices", [0, 1]))
