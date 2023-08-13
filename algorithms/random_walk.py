import random as coin
import numpy as np
from collections import Counter
from tqdm import tqdm
#TODO actually it is random walk on infinite line but for now it is only possible option
#It will be more general in the future


#Idea for make algorithm faster from
# https://stackoverflow.com/questions/76842017/is-there-a-way-to-make-the-code-exploring-random-walk-in-1-d-space-more-optimal


def run(initial_pos,iterations,trials):
    result = Counter()
    coin = np.random.default_rng()
    result_update = result.update
    for _ in tqdm(range (trials),
                  desc="Trials"):
        result_update([initial_pos + 2 * coin.choice(2,size=iterations).sum() - iterations])
    return result
