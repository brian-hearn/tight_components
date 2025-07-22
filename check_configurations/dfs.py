from cconf_checking_functions import *

counters = None

# Depth-first search
def dfs(triple_dict, COLOURS, output_progress, S, T, counters, index=0):
    # Set up counters
    # steps counts the number of times depth increases
    # configurations_checked counts the number of times a configuration is ruled out
    if counters is None:
        counters = {'steps': 0, 'configurations_checked': 0}

    counters['steps'] += 1
    if index == len(T):
        if fewer_than_three_occurences(triple_dict, COLOURS):
            # print('Configuration contains fewer than three occurences of some colour.')
            return {'result' : False, 'counters' : counters}
        # elif exactly_five_occurences(triple_dict, COLOURS):
        #     # print('Configuration contains exactly five occurences of some colour.')
        #     return False
        elif check_pair_in_four_colours(triple_dict):
            return {'result' : False, 'counters' : counters}
        else:
            return {'result' : True, 'counters' : counters}
    
    # Select triple
    t = T[index]

    # Skip over selected triple if it has already been assigned a colour
    if triple_dict[tuple(sorted(t))] is not None:
        return dfs(triple_dict, COLOURS, output_progress, S, T, counters, index + 1)

    valid_cols = [c for c in COLOURS if c not in t]
    for colour in valid_cols:
        triple_dict[tuple(sorted(t))] = colour
        valid = True
            
        for q in find_valid_quadruples(t, triple_dict, S):
            if is_rainbow(triple_dict, *q):
                valid = False
                if output_progress:
                    if counters['configurations_checked'] % output_progress == 0:
                        print("Configurations checked: " + str(counters['configurations_checked']) + ". Triples currently coloured: " + str(index) + " out of " + str(len(T)) + ".")
                        # print('Coloured ' + str(index) + " out of " + str(len(T)) + ".")
                counters['configurations_checked'] += 1
                break

        if valid:
            if dfs(triple_dict, COLOURS, output_progress, S, T, counters, index + 1)['result']:
                return {'result' : True, 'counters' : counters}

        triple_dict[tuple(sorted(t))] = None  # Reset colour to None
    return {'result' : False, 'counters' : counters} # Backtrack