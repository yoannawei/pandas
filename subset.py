import sys

for line in sys.stdin:
    print(line, end="")

    import numpy as np

    test1 = np.array[[Dan, 3], [Emily, 5], [Dan, 8], [Emily, 21], [Fred, 6], [Emily, 12]]

    record = {}
    count = {}

    # calculate daily average for each person
    for i, j in test1:
        record['i'] += j
        count['i'] += 1

    avg = {}

    avg['i'] = record['i'] / count['i']

    # get the largest daily average
    max = 0
    for i, j in avg.items():
        if j > max:
            max = j
            max_name = i

    # extract subset
    for s in subset:
        if s == max_name:
            print(s)
        else:
            print("None")
