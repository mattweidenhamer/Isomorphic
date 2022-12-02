import csv

class Matrix:
    def __init__(self, size, pairs, is_directed = False):
        self.size = size
        self.pairs = pairs
        self.matrix = []
        for i in range(self.size):
            newRow = []
            for j in range(self.size):
                newRow.append(0)
            self.matrix.append(newRow)
        for pair in pairs:
            self.matrix[pair.first][pair.second] = 1
            if not is_directed:
                self.matrix[pair.second][pair.first] = 1
    
    def add_row(self, row):
        if len(row) == self.size:
            self.matrix.append(row)
        else:
            Exception("Row size didn't match inherited rowsize!")

    def __str__(self):
        string = "Vertex\t\t"
        for i in range(self.size):
            string += f"{i}\t"
        string += "\n\n"
        counter = 0
        for row in self.matrix:
            string += f"{counter}\t\t"
            for item in row:
                string += f"{item}\t"
            string += "\n"
            counter += 1
        return string

    def save_to_file(self, file_location):
        with open(file_location, "x") as writeLocation:
            output = csv.writer(writeLocation, delimiter=",")
            for row in self.matrix:
                output.writerow(row)

    def solve(self, relationships, lexicon, matrix):
        # If the passed pairs converted by Lexicon equal this matrix, then it will succeed.
        trans_relationships = []
        for relationship in relationships:
            trans_relationships.append(Pairing(lexicon[relationship.first], lexicon[relationship.second]))
        test_matrix = Matrix(self.size, trans_relationships)
        if str(test_matrix) == str(self):
            return True
        return False
        # good_pairs = []
        # for pair in self.pairs:
        #     good_pairs.append(str(pair))
        # translated_relationships = []
        # iterations = 0
        # for relationship in relationships:
        #     #print(f"Added relationship {relationship}")
        #     iterations += 1
        #     translated_relationships.append(Pairing(lexicon[relationship.first], lexicon[relationship.second]))
        # removed = 0
        # for relationship in translated_relationships:
        #     if str(relationship) in good_pairs:
        #         removed += 1
        #         good_pairs.remove(str(relationship))
        #     else:
        #         #print(f"Failed after {removed} attempts out of the {iterations} relationships")
        #         return False
        # return True


    @staticmethod
    def get_relationships(rows):
        edges = []
        rowLocation = 0
        for row in rows:
            columnLocation = 0
            for value in (row):
                if int(value) == 1:
                    edges.append(Pairing(rowLocation, columnLocation))
                columnLocation += 1
            rowLocation += 1
        return edges

    @staticmethod
    def load_from_file(file_location):
        rows = []
        with open(file_location, "r") as input_object:
            reader = csv.reader(input_object, delimiter=",")
            for row in reader:
                if len(row) > 0:
                    values = []
                    for value in row:
                        values.append(value)
                    rows.append(values)
        return  Matrix(len(rows[0]), Matrix.get_relationships(rows))

class Pairing:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __str__(self):
        return f"{self.first} and {self.second}"

class Lexicon:
    def __init__(self, listing):
        self.pages = listing
    def __str__(self):
        count = 0
        string = ""
        for i in self.pages:
            string += f"Vertex {count} is an alias for vertice {i}\n"
            count += 1
        return string

class IteratingDict:
    def __init__(self, matrix1: Matrix, matrix2: Matrix, length: int):
        self.length = length
        self.dict = {}
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.used_values = []
        for i in range(length):
            self.dict[i] = 0

    def recursive_solver(self, index=0):
        if index >= self.length:
            if(self.matrix1.solve(self.matrix2.pairs, self.dict, self.matrix2)):
                return True
            return False
        else:
            for i in range(self.length):
                if i not in self.used_values:
                    self.used_values.append(i)
                    self.dict[index] = i
                    if(self.recursive_solver(index + 1)):
                        return True
                    self.used_values.remove(i)
        return False
        
    def __str__(self):
        return str(self.dict)

        

if __name__ == "__main__":
    location = input("What file would you like to test import?")
    test_matrix = Matrix.load_from_file(f"./{location}.csv")


