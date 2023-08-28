import numpy as np
from collections import Counter
from tqdm import tqdm

#Idea for make algorithm faster from
# https://stackoverflow.com/questions/76842017/is-there-a-way-to-make-the-code-exploring-random-walk-in-1-d-space-more-optimal


def run_line(initial_pos,steps,trials,begin,end):
    result = Counter()
    coin = np.random.default_rng()
    result_update = result.update
    for _ in tqdm(range (trials),
                  desc="Trials"):
        final_pos = initial_pos + 2 * coin.choice(2,size=steps).sum() - steps
        if final_pos < begin:
            final_pos = begin
        elif final_pos > end:
            final_pos = end
        result_update([final_pos])
    return result
