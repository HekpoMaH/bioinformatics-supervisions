import math
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
V = {CpG: [(math.log(0.5 * emission_matrix[CpG][indexing[sequence[0]]]), None)],
     non_CpG: [(math.log(0.5 * emission_matrix[non_CpG][indexing[sequence[0]]]), None)]
    }
iterseq = enumerate(sequence)
next(iterseq)
for _, el in iterseq:
    
    opt1 = math.log(transition_matrix[non_CpG][CpG]) + V[non_CpG][-1][0]
    opt0 = math.log(transition_matrix[CpG][CpG]) + V[CpG][-1][0]
    if opt1 > opt0:
        V[CpG].append((opt1 + math.log(emission_matrix[CpG][indexing[el]]), 1))
    else:
        V[CpG].append((opt0 + math.log(emission_matrix[CpG][indexing[el]]), 0))

    opt1 = math.log(transition_matrix[non_CpG][non_CpG]) + V[non_CpG][-1][0]
    opt0 = math.log(transition_matrix[CpG][non_CpG]) + V[CpG][-1][0]
    if opt1 > opt0:
        V[non_CpG].append((opt1 + math.log(emission_matrix[non_CpG][indexing[el]]), 1))
    else:                                  
        V[non_CpG].append((opt0 + math.log(emission_matrix[non_CpG][indexing[el]]), 0))

pp = pprint.PrettyPrinter(indent=4)
# trellis looks legit
pp.pprint(V)
i = 8
states = [CpG if V[CpG][len(sequence)-1][0] > V[non_CpG][len(sequence)-1][0] else non_CpG]
i -= 1
while i > 0:
    states.append(V[states[-1]][i][1])
    i-=1

print(['CpG' if state == 0 else 'non-CpG' for state in states])
# might be a bug (though I checked it several times) but the sequence I get is non-CpG only
