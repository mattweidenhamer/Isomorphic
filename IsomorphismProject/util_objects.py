import csv

class matrix:
    def __init__(self, rows, points):
        self.points = points
        self.matrix = []
        self.length = len(rows[0])
        for row in rows:
            self.addRow(row)
    
    def addRow(self, row):
        if len(row) == self.length:
            self.matrix.append(row)
        else:
            Exception("Row size didn't match inherited rowsize!")

    def __str__(self):
        string = "Vertex\t\t"
        for i in range(self.length):
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

class pairing:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def __str__(self):
        return f"{self.first} and {self.second}"


    