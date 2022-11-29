from random import randint
from util_objects import *

class AdjConstructor:


    def __init__(self) -> None:
        self.matrix1 = []
        self.matrix2 = []
        self.length = self.getLength()
        self.is_directed = self.relationshipType()
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
                            relationships.append(pairing(int(broken[0]), int(broken[2])))
                            print(f"Added point {broken[0]}, {broken[2]}. Add another, undo with Z, or stop with X")
                    else:
                        print("Please only use numbers in the form #, #. This includes the space..")
            print(f"Your graph of size {self.length} contains the following relationships:")
            for pair in relationships:
                print(pair)
            self.matrix1 = self.makeMatrixObject(relationships)
            print("Put into a matrix, it looks like this:")
            print(self.matrix1)
            isDone = input("If you are done, type D. Type anything else, and the program will let you add more relationships.\n").lower()
            if isDone == "d":
                break   
        return relationships
        

    def relationshipType(self):
        type = ""
        while type != "y" and type != "n":
            type = input("Is this a directed graph? Y/N ").lower()
        if type == "y":
            return True
        else:
            return False

        
    def getLength(self):
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

    def makeMatrixObject(self, pairs):
        rows = []
        for i in range(self.length):
            newRow = []
            for j in range(self.length):
                newRow.append(0)
            rows.append(newRow)
        for pair in pairs:
            rows[pair.first][pair.second] = 1
            if not self.is_directed:
                rows[pair.second][pair.first] = 1
        return matrix(rows, pairs)

    def jumble(self):
        print("Creating a lexicon.")
        pairs = self.matrix1.points
        length = self.matrix1.length
        lexicon = [None] * (length)
        for i in range(length):
            locationForI = randint(0, length - 1)
            while lexicon[locationForI] is not None:
                if locationForI >= len(lexicon) - 1:
                    locationForI = 0
                else:
                    locationForI += 1
            lexicon[locationForI] = i
            print(f"Added alias for {i}")

        print("Jumbling up the relations.")
        relationsButEvil = []
        for pair in pairs:
            relationsButEvil.append(pairing(lexicon[pair.first], lexicon[pair.second]))

        print("Building a second matrix.")
        self.matrix2 = self.makeMatrixObject(relationsButEvil)
        

        

    def build(self):
        name = input("What would you like to name this matrix?")
        print("Writing first matrix.")
        with open(f"./output/{name}.csv", "x") as writeLocation:
            output = csv.writer(writeLocation, delimiter=",")
            for row in self.matrix1.matrix:
                output.writerow(row)
        print("Writing second matrix.")
        with open(f"./output/{name} jumble.csv", "x") as writeLocation:
            output = csv.writer(writeLocation, delimiter=",")
            for row in self.matrix2.matrix:
                output.writerow(row)
        print("Successfully wrote both matrixes to output folder.")

if __name__ == "__main__":
    AdjConstructor()
        
