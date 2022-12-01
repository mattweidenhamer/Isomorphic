from random import randint
from util_objects import *

class AdjConstructor:
    # Honestly this really shouldnt be a class aaa
    def __init__(self) -> None:
        self.matrix1 = None
        self.matrix2 = None
        self.length = self.get_length()
        self.is_directed = self.relationship_type()
        self.index = self.get_relationships()

        self.jumble()
        self.build()
    
    def get_relationships(self):
        relationships = []
        while(True):
            print("Please enter a relationship, in the form of '#, #' (including the comma, but not the ').\nTo stop adding relationships, type X. To remove the last, type Z\n"
                + f"{'' if self.is_directed else 'Note that since this is not a directed graph, you should only add each pair once, since sharing is implied.'}" )
            while(True):
                value = input()
                if value.lower() == "x":
                    break
                elif value.lower() == "z":
                    relationships.pop()
                    print("Removed last relationship.")
                else:
                    broken = value.partition(", ")
                    if broken[0].isdigit() and broken[2].isdigit():
                        if int(broken[0]) > self.length - 1 or int(broken[2]) > self.length - 1:
                            print("One of the values provided is greater than the number of vertices provided (note: Vertex numbering starts at zero, not one)")
                        else:
                            relationships.append(Pairing(int(broken[0]), int(broken[2])))
                            print(f"Added point {broken[0]}, {broken[2]}. Add another, undo with Z, or stop with X")
                    else:
                        print("Please only use numbers in the form #, #. This includes the space..")
            print(f"Your graph of size {self.length} contains the following relationships:")
            for pair in relationships:
                print(pair)
            self.matrix1 = Matrix(self.length, relationships)
            print("Put into a matrix, it looks like this:")
            print(self.matrix1)
            if input("If you are done, type D. Type anything else, and the program will let you add more relationships.\n").lower() == "d":
                break
        return relationships


    def relationship_type(self):
        r_type = ""
        while r_type != "y" and r_type != "n":
            r_type = input("Is this a directed graph? Y/N ").lower()
        if r_type == "y":
            return True
        else:
            return False

        
    def get_length(self):
        length = 16
        maxlength = 15
        while length > maxlength:
            length = input("Enter the number of vertices. ")
            if not length.isdigit():
                print("Please use only numbers")
            else:
                length = int(length)
                if length > maxlength:
                    print("That is too many! For the sake of process time, you cannot have move than 15.")
        return length

    def jumble(self):
        print("Creating a lexicon.")
        pairs = self.matrix1.pairs
        length = self.matrix1.size
        lexicon = [None] * (length)
        for i in range(length):
            location_for_i = randint(0, length - 1)
            while lexicon[location_for_i] is not None:
                if location_for_i >= len(lexicon) - 1:
                    location_for_i = 0
                else:
                    location_for_i += 1
            lexicon[location_for_i] = i
            print(f"Added alias for {i}")

        print("Jumbling up the relations.")
        relations_but_evil = []
        for pair in pairs:
            relations_but_evil.append(Pairing(lexicon[pair.first], lexicon[pair.second]))

        print("Building the second matrix.")
        self.matrix2 = Matrix(self.matrix1.size, relations_but_evil)

    def build(self):
        name = input("What would you like to name this matrix? ")
        print("Writing first matrix.")
        self.matrix1.save_to_file(f"./output/{name}.csv")
        print("Writing second matrix.")
        self.matrix2.save_to_file(f"./output/{name} jumble.csv")
        print("Successfully wrote both matrixes to output folder.")

if __name__ == "__main__":
    AdjConstructor()