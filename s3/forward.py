import numpy as np
import pprint

CpG = 0
non_CpG = 1
transition_matrix = [[0.4, 0.6], [0.5, 0.5]]
emission_matrix = {0: [0.2, 0.3, 0.3, 0.2], 1: [0.3, 0.2, 0.2, 0.3]}
indexing = {'A':0, 'C':1, 'G':2, 'T':3}
sequence = 'GGCACTGAA'
print([c for c in sequence])
#I skipped adding imaginary 0 state
f = {CpG: [0.5 * emission_matrix[CpG][indexing[sequence[0]]]],
     non_CpG: [0.5 * emission_matrix[non_CpG][indexing[sequence[1]]]]
    }
iterseq = enumerate(sequence)
next(iterseq)
for i,el in iterseq:
    f[CpG].append(
        (
            transition_matrix[non_CpG][CpG] * f[non_CpG][-1] +
            transition_matrix[CpG][CpG] * f[CpG][-1]
        ) *
        emission_matrix[CpG][indexing[el]]
    )
    f[non_CpG].append(
        (
            transition_matrix[non_CpG][non_CpG] * f[non_CpG][-1] +
            transition_matrix[CpG][non_CpG] * f[CpG][-1]
        ) *
        emission_matrix[non_CpG][indexing[el]]
    )

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(f[CpG])
pp.pprint(f[non_CpG])

print("Prob is", f[CpG][-1] * 0.5 + f[non_CpG][-1] * 0.5)
