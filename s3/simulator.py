import numpy as np
CpG = 0
non_CpG = 1
transition_matrix = [[0.5, 0.5], [0.4, 0.6]]
# check this out
print("Just an example",transition_matrix[non_CpG])
state = np.random.choice([CpG,non_CpG]) # probabilites are uniform
for _ in range(50):
    # Cheeky, huh?
    state = np.random.choice([CpG,non_CpG], p=transition_matrix[state])
    # brackets for readability
    print("(CpG)" if state == 0 else "(non-CpG)", end=' ')
print()
