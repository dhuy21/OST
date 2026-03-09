import random
import math


def random_strategy(K, s, n, t):
    return random.randint(0, K - 1)


def epsilon_greedy(K, s, n, t, epsilon=0.1):
    if random.random() < epsilon:
        return random.randint(0, K - 1)
    mu_hat = [s[i] / n[i] for i in range(K)]
    return mu_hat.index(max(mu_hat))


def epsilon_greedy_decreasing(K, s, n, t):
    epsilon = 1.0 / math.log(t ** 2)
    if random.random() < epsilon:
        return random.randint(0, K - 1)
    mu_hat = [s[i] / n[i] for i in range(K)]
    return mu_hat.index(max(mu_hat))


def ucb(K, s, n, t):
    scores = []
    for i in range(K):
        mu_hat = s[i] / n[i]
        exploration = math.sqrt(2 * math.log(t) / n[i])
        scores.append(mu_hat + exploration)
    return scores.index(max(scores))
