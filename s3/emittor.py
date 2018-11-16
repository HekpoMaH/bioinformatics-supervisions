import numpy as np
f = open("chain", "r")
emission_matrix = {"(CpG)": [0.2, 0.3, 0.3, 0.2], "(non-CpG)": [0.3, 0.2, 0.2, 0.3]}
print(*[(state, np.random.choice(['A', 'C', 'G', 'T'], p=emission_matrix[state])) for state in f.read().split()], sep="\n")
