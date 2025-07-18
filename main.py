# from itertools import combinations
from setup_functions import *
from checking_functions import *

# Depth-first search
def dfs(triple_dict, COLOURS, output_progress, index=0):
    global step_counter
    global configurations_checked_counter
    step_counter += 1
    if index == len(T):
        if fewer_than_three_occurences(triple_dict, COLOURS):
            # print('Configuration contains fewer than three occurences of some colour.')
            return False
        # elif exactly_five_occurences(triple_dict, COLOURS):
        #     # print('Configuration contains exactly five occurences of some colour.')
        #     return False
        elif check_pair_in_four_colours(triple_dict):
            return False
        else:
            return True
    
    # Select triple
    t = T[index]

    # Skip over selected triple if it has already been assigned a colour
    if triple_dict[tuple(sorted(t))] is not None:
        return dfs(triple_dict, COLOURS, output_progress, index + 1)

    valid_cols = [c for c in COLOURS if c not in t]
    for colour in valid_cols:
        triple_dict[tuple(sorted(t))] = colour
        valid = True
            
        for q in find_valid_quadruples(t, triple_dict, S):
            if is_rainbow(triple_dict, *q):
                valid = False
                if output_progress:
                    if configurations_checked_counter % output_progress == 0:
                        print("Configurations checked: " + str(configurations_checked_counter) + ". Triples currently coloured: " + str(index) + " out of " + str(len(T)) + ".")
                        # print('Coloured ' + str(index) + " out of " + str(len(T)) + ".")
                configurations_checked_counter += 1
                break

        if valid:
            if dfs(triple_dict, COLOURS, output_progress, index + 1):
                return True

        triple_dict[tuple(sorted(t))] = None  # Reset colour to None

    return False # Backtrack

# Main logic for checking cases
def check_case(triple_dict, COLOURS, output_progress):
    if dfs(triple_dict, COLOURS, output_progress):
        print("Valid configuration found!")
        for k in sorted(triple_dict):
            print(f"{k}: {triple_dict[k]}")
        print("Steps: " + str(step_counter))
        print("Configurations checked: " + str(configurations_checked_counter))
        return True
    else:
        print("No valid configuration exists.")
        print("Steps: " + str(step_counter))
        print("Configurations checked: " + str(configurations_checked_counter))
        return False

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

results = []
case_counter = 1
step_counter = 0 # Counts number of times depth increases
configurations_checked_counter = 0 # Counts number of times a configuration is ruled out
# Print to console every time output_progress configurations have been checked. Set to False for no output.
output_progress = False
# output_progress = 25000

for case in cases:
    print('---------- CASE ' + str(case_counter) + " OF " + str(len(cases)) + " ----------")
    case_counter += 1
    # If extra_vertex is True, check if two triples overlapping in two vertices were assigned two different colours
    if check_initial_overlap(case, extra_vertex):
        results.append(("Error","N/A","N/A"))
        reset_dict(triple_dict)
        step_counter = 0
        configurations_checked_counter = 0
    # Check if a triple was assigned a colour contained in the triple
    elif check_for_illegitimate_colours(case):
        results.append(("Error","N/A","N/A"))
        reset_dict(triple_dict)
        step_counter = 0
        configurations_checked_counter = 0
    else:
        for tuple_of_triples in case:
            for triple in tuple_of_triples:
                if 'v' in S:
                    fill_triangle(triple_dict, triple, case[tuple_of_triples])
                else:
                    triple_dict[tuple(sorted(triple))] = case[tuple_of_triples]
        # Check if there is a rainbow K_4^{(3)}
        if check_current_configuration(triple_dict):
            print("Initialisation error: Rainbow in initial configuration.")
            results.append(("Error","N/A","N/A"))
            reset_dict(triple_dict)
            step_counter = 0
            configurations_checked_counter = 0
        else:
            # Run depth-first search
            outcome = check_case(triple_dict, COLOURS, output_progress = output_progress)
            results.append((outcome,step_counter,configurations_checked_counter))
            reset_dict(triple_dict)
            step_counter = 0
            configurations_checked_counter = 0
        
print("---------- SUMMARY ---------- ")
print("Number of colours used: " + str(len(COLOURS)))
print("Extra vertex: " + str(extra_vertex))
print("Number of cases checked: " + str(len(cases)))
print("Number of cases with a valid configuration: " + str(sum(1 for value, _, _ in results if value == True)))
print("Number of cases with no valid configuration: " + str(sum(1 for value, _, _ in results if not value)))
print("Number of cases with an initialisation error: " + str(sum(1 for value, _, _ in results if value == "Error")))
print("Full results (outcome, number of steps, number of configurations checked):")
print(results)