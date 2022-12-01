from make_isomorphic import AdjConstructor
from util_objects import *

# How to solve to see if the relationships are the same 

# Optional: Add timer for how long to work.

def checker(file_1, file_2):
    def recursive_solver(dictionary, position):
        if len(dictionary) >= matrix2.size:
            # Filter all relationships to lexicon, and then compare the values
            if matrix2.solve(matrix1.pairs, dictionary):
                return dictionary
            return None
        # Generate a lexicon (algorithmically, not randomly)
        #   Start with default, then jumble values from the last vertex in the lexicon

        #This part needs to be finished
        for i in range(matrix2.size - len(dictionary) - 1):
            i += position
            if position >= len(dictionary):
                position = 0
            dictionary.add(i, position)
            new_dict = recursive_solver(dictionary, position + 1)
            if not new_dict:
                return new_dict
        return None
        
    # Import all points
    matrix1 = Matrix.load_from_file(file_1)
    matrix2 = Matrix.load_from_file(file_2)
    for i in range(matrix2.size):
        lexicon = recursive_solver({str(i): "0"}, i)
        if lexicon != None:
            break
    if lexicon != None:
        print("Solution found using the following lexicon:")
        print(Lexicon(lexicon))
        new_pairs = []
        for pair in matrix2.pairs:
            new_pairs.append(Pairing(lexicon[str(pair.first)], lexicon[str(pair.second)]))
        solved_matrix = Matrix(matrix2.size, new_pairs)
        print(f"Solved matrix looks like thus:\n{solved_matrix}")
    

if __name__ == "__main__":
    checker("./output/Test values.csv", "./output/Test values jumble.csv")
