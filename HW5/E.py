import numpy as np

class ImageProcessor:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def apply_command(self, command):
        parts = command.split()

        if parts[0] == "ROTATE":
            # 90 degrees clockwise: transpose + reverse each row
            self.matrix = np.rot90(self.matrix, -1)

        elif parts[0] == "TRANSPOSE":
            self.matrix = self.matrix.T

        elif parts[0] == "MULTIPLY":
            x = int(parts[1])
            self.matrix = self.matrix * x

    def get_matrix(self):
        return self.matrix

R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

K = int(input())
commands = [input().strip() for _ in range(K)]

processor = ImageProcessor(matrix)

for cmd in commands:
    processor.apply_command(cmd)

result = processor.get_matrix()

print(result.shape[0], result.shape[1])
for row in result:
    print(*row)