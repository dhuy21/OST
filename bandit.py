import time


def run_bandit(env, N, algorithm):
    K = env.K
    s = [0] * K
    n = [0] * K

    for i in range(K):
        r = env.pull(i)
        s[i] = r
        n[i] = 1

    for t in range(K + 1, N + 1):
        i_m = algorithm(K, s, n, t)
        r = env.pull(i_m)
        s[i_m] = s[i_m] + r
        n[i_m] = n[i_m] + 1

    return sum(s)


def run_bandit_benchmark(env, N_max, algorithm, checkpoints):
    K = env.K
    s = [0] * K
    n = [0] * K
    cumulative = 0
    sorted_cps = sorted(checkpoints)
    cp_idx = 0
    rewards = []
    times = []

    start = time.time()

    for i in range(K):
        r = env.pull(i)
        s[i] = r
        n[i] = 1
        cumulative += r

    for t in range(K + 1, N_max + 1):
        i_m = algorithm(K, s, n, t)
        r = env.pull(i_m)
        s[i_m] = s[i_m] + r
        n[i_m] = n[i_m] + 1
        cumulative += r

        if cp_idx < len(sorted_cps) and t == sorted_cps[cp_idx]:
            rewards.append(cumulative)
            times.append(time.time() - start)
            cp_idx += 1

    return rewards, times
