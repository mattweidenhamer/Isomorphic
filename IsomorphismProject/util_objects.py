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

    def solve(self, relationships: list, lexicon):
        good_pairs = self.pairs
        translated_relationships = []
        for relationship in relationships:
            translated_relationships.append(Pairing(lexicon[relationship.first], lexicon[relationship.second]))
        for relationship in translated_relationships:
            if relationship in good_pairs:
                good_pairs.remove(relationship)
            else:
                return False
        return True


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
    
        

if __name__ == "__main__":
    location = input("What file would you like to test import?")
    test_matrix = Matrix.load_from_file(f"./{location}.csv")
