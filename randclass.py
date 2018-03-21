import random

class RandomVariable(object):

    def __init__(self,dic):
        self.dic = dic

    def sample(self):
        rnd = random.random() * sum(self.dic.values())
        for k, v in self.dic.items():
            rnd -= v
            if rnd < 0:
                return k

    def all_outcomes(self):
        return list(self.dic.keys())


    def pmf(self,outcome):
        return self.dic[outcome]


die = {1: .5, 2: .5}

r1 = RandomVariable(die)

print(r1.pmf(1))
