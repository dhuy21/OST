import random


class BanditEnvironment:

    def __init__(self, means):
        self.means = means
        self.K = len(means)

    def pull(self, i):
        if random.random() < self.means[i]:
            return 1
        return 0
