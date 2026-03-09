from environment import BanditEnvironment
from algorithmes_A import random_strategy, epsilon_greedy, epsilon_greedy_decreasing, ucb
from bandit import run_bandit


def run_question1():
    means = [0.2, 0.4, 0.6, 0.8]
    K = len(means)
    N = 10000

    algorithms = {
        "random": random_strategy,
        "e-greedy": epsilon_greedy,
        "e-greedy-dec": epsilon_greedy_decreasing,
        "UCB": ucb,
    }

    best_mu = max(means)
    avg_mu = sum(means) / K

    print(f"\nScénario : K={K}, μ={means}, N={N}")
    print(f"  μ* = {best_mu}  →  reward max théorique = {best_mu * N:.0f}")
    print(f"  μ_moy = {avg_mu:.2f} →  reward random théorique ≈ {avg_mu * N:.0f}")
    print("-" * 60)

    for name, algo in algorithms.items():
        env = BanditEnvironment(means)
        reward = run_bandit(env, N, algo)
        print(f"  {name:15s} : cumulative reward = {reward}")


if __name__ == "__main__":
    run_question1()
