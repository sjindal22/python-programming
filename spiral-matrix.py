class Spiral:

  def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

spiral = Spiral()
matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
print(spiral.spiralOrder(matrix))
