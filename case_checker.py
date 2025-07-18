from dfs import *
from checking_functions import *
from setup_functions import *

# Checks an individual case
def check_case(triple_dict, COLOURS, output_progress, S, T, counters):
    outcome = dfs(triple_dict, COLOURS, output_progress, S, T, counters)
    if outcome['result']:
        print("Valid configuration found!")
        for k in sorted(triple_dict):
            print(f"{k}: {triple_dict[k]}")
        print("Steps: " + str(outcome["counters"]["steps"]))
        print("Configurations checked: " + str(outcome["counters"]["configurations_checked"]))
        return outcome
    else:
        print("No valid configuration exists.")
        print("Steps: " + str(outcome["counters"]["steps"]))
        print("Configurations checked: " + str(outcome["counters"]["configurations_checked"]))
        return outcome

def check_all_cases(cases, extra_vertex, triple_dict, output_progress, COLOURS, S, T):
    case_counter = 1
    results = []
    for case in cases:
        print('---------- CASE ' + str(case_counter) + " OF " + str(len(cases)) + " ----------")
        case_counter += 1
        # If extra_vertex is True, check if two triples overlapping in two vertices were assigned two different colours
        if check_initial_overlap(case, extra_vertex):
            results.append(("Error","N/A","N/A"))
            reset_dict(triple_dict)
        # Check if a triple was assigned a colour contained in the triple
        elif check_for_illegitimate_colours(case):
            results.append(("Error","N/A","N/A"))
            reset_dict(triple_dict)
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
            else:
                # Run depth-first search
                outcome = check_case(triple_dict, COLOURS, output_progress = output_progress, S = S, T = T, counters = counters)
                results.append((outcome["result"],outcome["counters"]["steps"],outcome["counters"]["configurations_checked"]))
                reset_dict(triple_dict)
    return results