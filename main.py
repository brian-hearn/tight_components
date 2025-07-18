# from itertools import combinations
from setup_functions import *
from checking_functions import *
from dfs import *
from case_checker import *

#####################
### CONFIGURATION ###
#####################
# COLOURS is the set of colours in the graph.
# Note that each element of COLOURS will refer to both a colour and a vertex which does not belong to the component of that colour.
# Colours can be assigned names arbitrarily, except that a colour may not be named 'v'.
COLOURS = ['R', 'G', 'B', 'Y', 'O', 'P']
# COLOURS = ['R', 'G', 'B', 'Y', 'O']

# S is the set of vertices to be considered.
# If extra_vertex is False, then the program will try to find valid configurations in the 'usual way'.
# If extra_vertex is True, an extra vertex will be added, which is allowed to (but does not necessarily) see every colour.
# In the latter case, the program will assume that any triple t whose colour is specified in the initial configuration of triple_dict forms an edge together with v.
# Hence all four subsets of t union {v} of size 3 will be automatically assigned this same colour.
extra_vertex = False
if extra_vertex:
    S = COLOURS + ['v']
else:
    S = COLOURS

# List of triples (subsets of size 3) from S.
T = sorted(list(combinations(S, 3)))

# Dictionary whose keys are triples from S and whose values are the colour associated with each triple (initialised to None).
triple_dict = {tuple(sorted(t)): None for t in T}

#############
# 6 colours #
#############

# cases is a list of cases to be considered sequentially.
# Each case is a dict whose keys are tuples of triples and whose values are the colour to which these triples should be assigned.

cases = []

# 1 colour (not possible if each triple must occur at least 3 times)
# cases += [
#     {(tup('GBP'), tup('BPY'), tup('PYG'), tup('YGB')) + (tup('OGY'), tup('OGB')) : 'R'},
#     {(tup('GBP'), tup('BPY'), tup('PYG'), tup('YGB')) + (tup('OGY'), tup('OBP')) : 'R'},
#     {(tup('GBP'), tup('BPY'), tup('PYG')) + (tup('OGY'), tup('OGP'), tup('OGB')) : 'R'},
#     {(tup('GBP'), tup('BPY'), tup('PYG')) + (tup('OGY'), tup('OBY'), tup('OPY')) : 'R'},
#     {(tup('GBP'), tup('BPY'), tup('PYG')) + (tup('OGY'), tup('OBY'), tup('OBP')) : 'R'},
#     {(tup('GBP'), tup('BPY'), tup('PYG')) + (tup('OGY'), tup('OGP'), tup('OPY')) : 'R'},
#     {(tup('GBP'), tup('BPY'), tup('PYG')) + (tup('OGY'), tup('OGP'), tup('OBY')) : 'R'}]

# 2 colours
cases += [{(tup('GBP'), tup('BPY'), tup('PYG'), tup('YGB')) : 'R',
     (tup('ROG'), tup('ROP')) : 'B'},
    {(tup('GBP'), tup('BPY'), tup('PYG'), tup('YGB')) : 'R',
     (tup('GBO'),) : 'R',
     (tup('ROY'),) : 'G'}
     ,
    {(tup('GBP'), tup('BPY'), tup('PYG')) : 'R',
     (tup('ROY'), tup('ROG'), tup('ROB')) : 'P'},
    {(tup('GBP'), tup('BPY'), tup('PYG')) : 'R',
     (tup('ROY'), tup('ROP'), tup('ROB')) : 'G'}
     ]

#############
# 5 colours #
#############

# Only possible case:
# cases = [{(tup('GBY'), tup('GOY')) : 'R',
#           (tup('ROB'),) : 'G'}]

# For testing:
# cases = [{(tup('GBY'), tup('GYO')) : 'R',
#           (tup('RYO'), tup('BYO')) : 'G',
#           (tup('RBO'), tup('GBO')) : 'Y',
#           (tup('RGB'), tup('RBY')) : 'O',
#           (tup('RGY'), tup('RGO')) : 'B'}]

# cases = [{}]

################
## Main logic ##
################

# Print to console every time output_progress configurations have been checked. Set to False for no output.
output_progress = False
# output_progress = 25000

results = check_all_cases(cases, extra_vertex, triple_dict, output_progress, COLOURS, S, T)
        
print("---------- SUMMARY ---------- ")
print("Number of colours used: " + str(len(COLOURS)))
print("Extra vertex: " + str(extra_vertex))
print("Number of cases checked: " + str(len(cases)))
print("Number of cases with a valid configuration: " + str(sum(1 for value, _, _ in results if value == True)))
print("Number of cases with no valid configuration: " + str(sum(1 for value, _, _ in results if not value)))
print("Number of cases with an initialisation error: " + str(sum(1 for value, _, _ in results if value == "Error")))
print("Full results (outcome, number of steps, number of configurations checked):")
print(results)