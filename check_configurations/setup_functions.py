# Functions for pre-assigning colours to triples
def tup(input):
    return tuple(sorted(input))

def fill_triangle(triple_dict, triple, K):
    A, B, C = triple
    v='v'
    triple_dict[tuple(sorted((A, B, C)))] = K
    triple_dict[tuple(sorted((v, B, C)))] = K
    triple_dict[tuple(sorted((A, v, C)))] = K
    triple_dict[tuple(sorted((A, B, v)))] = K
    return

# Function to reset dict between cases
def reset_dict(dict):
    for key in dict:
        dict[key] = None