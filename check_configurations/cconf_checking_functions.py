from itertools import combinations
from collections import Counter
from collections import defaultdict

# Given a triple, finds all quadruples of triples containing that triple
def find_valid_quadruples(t, triple_dict, S):
    fourth_elements = [x for x in S if x not in t]
    quadruples_of_triples = []
    for element in fourth_elements:
        quadruple = [t]
        for pair in combinations(t, 2):
            triple = tuple(sorted((element,) + pair))
            if triple_dict[tuple(sorted(triple))] != None:
                quadruple.append(tuple(sorted(triple)))
        # print(quadruple)
        if len(quadruple) == 4:
            quadruples_of_triples.append(quadruple)
    return quadruples_of_triples

# Checks if a quadruple of triples forms a rainbow
def is_rainbow(triple_dict, t1, t2, t3, t4):
    values = [
        triple_dict[tuple(sorted(t1))],
        triple_dict[tuple(sorted(t2))],
        triple_dict[tuple(sorted(t3))],
        triple_dict[tuple(sorted(t4))]
    ]
    return len(set(values)) == 4

# Checks if any colour occurs fewer than three times
def fewer_than_three_occurences(my_dict, MY_COLOURS):
    filtered_values = [value for triple, value in my_dict.items() if 'v' not in triple]
    counts = Counter(filtered_values)
    return any(counts[colour] < 3 for colour in MY_COLOURS)

# Checks if any colour occurs fewer than three times
def exactly_five_occurences(my_dict, MY_COLOURS):
    filtered_values = [value for triple, value in my_dict.items() if 'v' not in triple]
    counts = Counter(filtered_values)
    return any(counts[colour] == 5 for colour in MY_COLOURS)

# Checks if any pair occurs in four triples of four different colours
def check_pair_in_four_colours(my_dict):
    pair_to_triples = defaultdict(list)
    for triple in my_dict:
        for pair in combinations(triple, 2):
            pair = tuple(sorted(pair))  # treat ('a', 'b') same as ('b', 'a')
            pair_to_triples[pair].append(triple)
    for pair, triples in pair_to_triples.items():
        if len(triples) >= 4:
            values = {my_dict[t] for t in triples}
            if len(values) >= 4:
                # print("Found:", pair, "with triples:", triples, "and distinct values:", values)
                return True
    else:
        return False
    
# Checks if there is a rainbow K_4^{(3)} in the current configuration (used to check the initial configuration)
def check_current_configuration(my_dict):
    cleaned_dict = {k: v for k, v in my_dict.items() if v is not None}
    for quad in combinations(cleaned_dict.keys(), 4):
        if is_rainbow(my_dict, *quad):
            return True
    else:
        return False
    
# In extra_vertex case: checks if two triples in initial configuration share two vertices but have different colours
# Used to detect errors in initial configuration
def check_initial_overlap(dict, extra_vertex):
    if extra_vertex:
        keys = list(dict.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                key1, key2 = keys[i], keys[j]
                val1, val2 = dict[key1], dict[key2]
                if val1 != val2:
                    for triple1 in key1:
                        for triple2 in key2:
                            if len(set(triple1) & set(triple2)) >= 2:
                                print("Initialisation error: extra_vertex is True, but the following triples overlap in two vertices while having different colours:")
                                print(str(triple1) + " has colour " + str(val1) + ".")
                                print(str(triple2) + " has colour " + str(val2) + ".")
                                return True
    return False

# Detects whether a triple has been assigned an illegitimate colour
# Used to detect errors in initial configuration
def check_for_illegitimate_colours(dict):
    cleaned_dict = {k: v for k, v in dict.items() if v is not None}
    for triple_tuple, value in cleaned_dict.items():
            for triple in triple_tuple:
                if value in triple:
                    print("Initialisation error: The following triple was assigned an illegitimate colour:")
                    print(str(triple) + " has colour " + str(value) + ".")
                    return True
    return False