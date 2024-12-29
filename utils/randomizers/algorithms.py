import numpy as np


def generate_exponential_weights(n):
    weights = np.random.exponential(scale=1.0, size=n)
    weights /= weights.sum()
    return weights


def generate_power_law_weights(n, alpha=2.0):
    weights = np.power(np.arange(1, n + 1), -alpha)
    weights /= weights.sum()
    return weights


def generate_beta_weights(n, alpha=2.0, beta=5.0):
    weights = np.random.beta(alpha, beta, size=n)
    weights /= weights.sum()
    return weights


def generate_lognormal_weights(n, mean=0.0, sigma=1.0):
    weights = np.random.lognormal(mean, sigma, size=n)
    weights /= weights.sum()
    return weights


def generate_zipf_weights(n, a=1.0):
    ranks = np.arange(1, n + 1)
    weights = 1 / np.power(ranks, a)
    weights /= weights.sum()
    return weights
