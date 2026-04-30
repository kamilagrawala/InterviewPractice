from itertools import zip_longest
class ListComprehensionPractice:
    def __init__(self):
        self.matrix = [[1,2,3],[4,5,6], [7,8]]
        self.flat = []
        self.square_list = []
        self.filtered_list = []
        self.transpose_list = []

    def flattenList(self, matrix):
        # List comprehension: Flatten list
        self.flat = [item for row in matrix for item in row]
        self.print(self.flat)

    def square(self, array):
        self.square_list = [pow(row, 2) for row in array]
        print(self.square_list)

    def filter(self, array):
        self.filtered_list = [i for i in array if i % 2 == 0]
        print(self.filtered_list)

    def transpose(self, matrix):
        max_len = max(len(row) for row in matrix)
        self.transpose_list = [[row[i] if i < len(row) else '.' for row in matrix] for i in range(max_len)]
        print(self.transpose_list)

    def print(self, matrix):
        print(f"{matrix}")

def main():
    # Instantiate and call your solution
    comp = ListComprehensionPractice()
    print("Running ListComprehension...")
    comp.print(comp.matrix)
    comp.flattenList(comp.matrix)
    comp.square(comp.flat)
    comp.filter(comp.square_list)
    comp.transpose(comp.matrix)


if __name__ == "__main__":
    main()
