from util_objects import *

# How to solve to see if the relationships are the same 

# Optional: Add timer for how long to work.

def checker(file_1, file_2):
    # Import all points
    print("Loading matrix 1.")
    matrix1 = Matrix.load_from_file(file_1)
    print("Loading Matrix 2.")
    matrix2 = Matrix.load_from_file(file_2)
    # Put into an iteratingdict
    
    iter_dict = IteratingDict(matrix1, matrix2, matrix1.size)
    is_valid = iter_dict.recursive_solver()
    if(is_valid):
        print("Solution found using the following lexicon:")
        print(iter_dict)
        new_pairs = []
        for pair in matrix2.pairs:
            new_pairs.append(Pairing(iter_dict.dict[pair.first], iter_dict.dict[pair.second]))
        solved_matrix = Matrix(matrix2.size, new_pairs)
        print(f"Solved matrix looks like thus:\n{solved_matrix}")
    else:
        print("No valid solution could be found to the dictionary.")
    

if __name__ == "__main__":
    to_check = input("Enter the name of the set you would like to check the values of.")
    checker(f"./output/{to_check}.csv", f"./output/{to_check} jumble.csv")
