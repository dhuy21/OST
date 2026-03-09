import os
import matplotlib.pyplot as plt
from environment import BanditEnvironment
from algorithmes_A import random_strategy, epsilon_greedy, epsilon_greedy_decreasing, ucb
from bandit import run_bandit_benchmark

NUM_RUNS = 100
N_MAX = 1_000_000
STEP = 100_000
CHECKPOINTS = list(range(STEP, N_MAX + 1, STEP))

MEANS = [0.1, 0.2, 0.3, 0.4, 0.5]

ALGORITHMS = [
    ("UCB",          ucb,                       "o"),
    ("e-greedy-dec", epsilon_greedy_decreasing,  "s"),
    ("e-greedy",     epsilon_greedy,             "^"),
    ("random",       random_strategy,            "D"),
]


def run_question2():
    print(f"Benchmark : K={len(MEANS)}, mu={MEANS}, N_max={N_MAX}, {NUM_RUNS} runs")

    avg_rewards, avg_times = compute_benchmark()

    os.makedirs("figures", exist_ok=True)
    generate_figures(avg_rewards, avg_times)

    print("Figures sauvegardees dans figures/")


def compute_benchmark():
    num_cp = len(CHECKPOINTS)
    avg_rewards = {}
    avg_times = {}

    for name, algo, _ in ALGORITHMS:
        avg_rewards[name] = [0.0] * num_cp
        avg_times[name] = [0.0] * num_cp

        print(f"  {name} ...", end=" ", flush=True)

        for _ in range(NUM_RUNS):
            env = BanditEnvironment(MEANS)
            rewards, times = run_bandit_benchmark(env, N_MAX, algo, CHECKPOINTS)
            for j in range(num_cp):
                avg_rewards[name][j] += rewards[j]
                avg_times[name][j] += times[j]

        for j in range(num_cp):
            avg_rewards[name][j] /= NUM_RUNS
            avg_times[name][j] /= NUM_RUNS

        print("OK")

    return avg_rewards, avg_times


def generate_figures(avg_rewards, avg_times):
    fig1, ax1 = plt.subplots()
    for name, _, marker in ALGORITHMS:
        ax1.plot(CHECKPOINTS, avg_rewards[name], marker=marker, label=name, markersize=5)
    ax1.set_xlabel("Number of pulls")
    ax1.set_ylabel("Cumulative reward")
    ax1.ticklabel_format(axis='y', style='plain')
    ax1.legend()
    fig1.tight_layout()
    fig1.savefig("figures/q2_cumulative_reward.png", dpi=150)
    plt.close(fig1)

    fig2, ax2 = plt.subplots()
    for name, _, marker in ALGORITHMS:
        ax2.plot(CHECKPOINTS, avg_times[name], marker=marker, label=name, markersize=5)
    ax2.set_xlabel("Number of pulls")
    ax2.set_ylabel("Time (in seconds)")
    ax2.legend()
    fig2.tight_layout()
    fig2.savefig("figures/q2_time.png", dpi=150)
    plt.close(fig2)


if __name__ == "__main__":
    run_question2()
