from IsomorphismProject.util_objects import *

def test_load_matrix():
    debug_pairs = [
        (0, 1),
        (0, 2),
        (0, 4),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4)
    ]
    relationships = []
    for i in debug_pairs:
        relationships.append(Pairing(i[0], i[1]))
    expected_matrix = Matrix(5, relationships)
    loaded_matrix = Matrix.load_from_file("./output/Test values.csv")
    assert str(loaded_matrix) == str(expected_matrix)