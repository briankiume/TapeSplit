import numpy as np


def minimal(a):
    a_len = len(a)
    parts = []
    for x in range(a_len):
        parts.append([a[:x + 1], a[x + 1:]])

    all = dict()
    diffs = []
    for part in parts[:-1]:
        summed = []
        for one in part:
            summed.append(np.sum(one))
        diff = abs(summed[1] - summed[0])
        diffs.append(diff)
        all[diff] = summed

    z = min(diffs)
    return z


print(minimal([3, 1, 2, 4, 3]))
