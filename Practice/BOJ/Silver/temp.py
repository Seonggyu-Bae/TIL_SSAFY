import random
import time

def choose(howmany):
    results = []
    for _ in range(howmany):
        num_list = [x for x in range(1, 46)]
        picked = []
        random.shuffle(num_list)
        for _ in range(6):
            start_time = time.time()
            time_interval = random.uniform(4.0, 5.1)
            while time.time() - start_time < time_interval:
                random.shuffle(num_list)
            picked.append(num_list.pop(0))

        results.append(sorted(picked))
    return results


for x in choose(1):
    print(x)
