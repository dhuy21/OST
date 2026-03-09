import random
import math
from environment import BanditEnvironment
from bandit import run_bandit
from algorithmes_A import ucb


def secret_share(value):
    part1 = random.uniform(-1000, 1000)
    part2 = value - part1
    return part1, part2


def run_secure_ucb(means, N):
    K = len(means)
    env = BanditEnvironment(means)

    # Serveur 1 et Serveur 2 : chacun stocke une part des sommes
    s1 = [0.0] * K
    s2 = [0.0] * K
    n = [0] * K

    for i in range(K):
        r = env.pull(i)
        p1, p2 = secret_share(r)
        s1[i] = p1
        s2[i] = p2
        n[i] = 1

    for t in range(K + 1, N + 1):
        # Calcul conjoint UCB (en vrai : via MPC, ici on simule)
        scores = []
        for i in range(K):
            mu = (s1[i] + s2[i]) / n[i]
            expl = math.sqrt(2 * math.log(t) / n[i])
            scores.append(mu + expl)
        arm = scores.index(max(scores))

        r = env.pull(arm)
        p1, p2 = secret_share(r)
        s1[arm] += p1
        s2[arm] += p2
        n[arm] += 1

    return s1, s2, n


def run_partie2():
    means = [0.2, 0.5, 0.8]
    K = len(means)
    N = 10000

    env = BanditEnvironment(means)
    reward_std = run_bandit(env, N, ucb)

    s1, s2, n = run_secure_ucb(means, N)
    reward_sec = sum(s1[i] + s2[i] for i in range(K))

    print(f"K={K}, mu={means}, N={N}")
    print(f"UCB standard       : reward = {reward_std}")
    print(f"UCB secret sharing : reward = {reward_sec:.0f}")
    print()
    print("Exemple -- ce que voit chaque serveur (bras 0) :")
    print(f"  Serveur 1 : s1[0] = {s1[0]:+.2f}")
    print(f"  Serveur 2 : s2[0] = {s2[0]:+.2f}")
    print(f"  Vrai s[0]        = {s1[0] + s2[0]:.0f}")
    print()
    print("Les parts sont aleatoires, aucun serveur ne connait les vrais rewards.")


if __name__ == "__main__":
    run_partie2()
