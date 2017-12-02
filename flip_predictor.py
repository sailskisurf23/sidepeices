from __future__ import division

#There is a bag containing coins. Each coin has a different "load" (probability it will land on heads on any given flip).
#You draw a coin (you don't know which one) and flip it a number of times and record the result.
#Write a program that returns a list that contains the probability that the next flip is heads after
#   each flip

def flip_predictor(prob_coins,coins):
    """
    Takes in:
        "Coins" is a list: Contains the probability each coin will land heads-up on any given flip. The "load" for each coin.
        "Prob_coins" is a list: Contains the the probabilities that the coin you are flipping is "this" coin (indexed the same as 'Coins').
    Returns:
        "prob" is a float: contains the probability that the next flip is heads."""
    prob = 0
    for x in range(len(prob_coins)):
        prob += prob_coins[x] * coins[x]
    return prob

def update_probs(flip,prob_coins,coins):
    """Based on the last flip, this function updates "prob_coins" using Bayes theorem
    "Flips" is a string: Contains the result of each flip so far.
"""
    if flip == 'H':
        joint_prob_sum = 0
        for x in range(len(prob_coins)):
            joint_prob_sum += (prob_coins[x] * coins[x])
        new_prob_coins = []
        for x in range(len(prob_coins)):
            new_prob_coin = prob_coins[x] * coins[x] / joint_prob_sum
            new_prob_coins.append(new_prob_coin)
        return new_prob_coins
    else:
        joint_prob_sum = 0
        for x in range(len(prob_coins)):
            joint_prob_sum += (prob_coins[x] * (1-coins[x]))
        new_prob_coins = []
        for x in range(len(prob_coins)):
            new_prob_coin = (prob_coins[x] * (1-coins[x])) / joint_prob_sum
            new_prob_coins.append(new_prob_coin)
        return new_prob_coins

coins = [0.14,0.32,0.42,0.81,0.21]
flips = 'HHHTTTHHH'
n = len(coins)
prob_coins = [1/n]*n

predictions = []
for flip in flips:
    prob_coins = update_probs(flip,prob_coins,coins)
    predictions.append(flip_predictor(prob_coins,coins))

print(predictions)

#testcases=[
#(([0.5,0.4,0.3],'HHTH'),[0.4166666666666667, 0.432, 0.42183098591549295, 0.43639398998330553]),
#(([0.14,0.32,0.42,0.81,0.21],'HHHTTTHHH'),[0.5255789473684211, 0.6512136991788505, 0.7295055220497553, 0.6187139453483192, 0.4823974597714815, 0.3895729901052968, 0.46081730193074644, 0.5444108434105802, 0.6297110187222278]),
#(([0.14,0.32,0.42,0.81,0.21],'TTTHHHHHH'),[0.2907741935483871, 0.25157009005730924, 0.23136284577678012, 0.2766575695593804, 0.3296000585271367, 0.38957299010529806, 0.4608173019307465, 0.5444108434105804, 0.6297110187222278]),
#(([0.12,0.45,0.23,0.99,0.35,0.36],'THHTHTTH'),[0.28514285714285714, 0.3378256513026052, 0.380956725493104, 0.3518717367468537, 0.37500429586037076, 0.36528605387582497, 0.3555106542906013, 0.37479179323540324]),
#(([0.03,0.32,0.59,0.53,0.55,0.42,0.65],'HHTHTTHTHHT'),[0.528705501618123, 0.5522060353798126, 0.5337142767315369, 0.5521920592821695, 0.5348391689038525, 0.5152373451083692, 0.535385450497415, 0.5168208803156963, 0.5357708613431963, 0.5510509656933194, 0.536055356823069])]
