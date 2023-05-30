import random
import numpy as np

class MacMahonSquares():
    def __init__(self, height=4, width=6, colors=3) -> None:
        self.width = width
        self.height = height
        self.squares = 4
        self.colors = []
        for i in range(colors):
            self.colors.append(i+1)
        self.array = np.zeros((height, width, 4), dtype=int)
        self.bool_array = np.zeros((height, width, 4), dtype=bool)

    def randomize(self):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(self.squares):
                    self.array[i][j][k] = self.colors[random.randint(0, len(self.colors)-1)]
    
    def print(self):
        for j in range(self.width):
            print(end='| ')
            print('^', end=' ')
            print('>', end=' ')
            print('v', end=' ')
            print('<', end=' ')
        print('|')
        
        print('-'*(self.width*10+1))
        for i in range(self.height):
            for j in range(self.width):
                print(end='| ')
                for k in range(self.squares):
                    print(self.array[i][j][k], end=' ')
                
            print('|')
            print('-'*(self.width*10+1))
        print()

    def swap(self, coord1, coord2):
        #swap random squares
        i1, j1, k1 = coord1
        i2, j2, k2 = coord2

        temp = self.array[i1][j1][k1]
        self.array[i1][j1][k1] = self.array[i2][j2][k2]
        self.array[i2][j2][k2] = temp

    def swap_random(self):
        coord1 = [random.randint(0, self.height-1), random.randint(0, self.width-1), random.randint(0, self.squares-1)]
        coord2 = [random.randint(0, self.height-1), random.randint(0, self.width-1), random.randint(0, self.squares-1)]
        self.swap(coord1, coord2)

    def sum_square(self, squares=False):
        suma = 0
        sum_border = 0
        border = self.array[0][0][0]
        self.bool_array *= False
        
        # The border
        for i in range(self.width):
            if self.array[0][i][0] == border:
                sum_border += 1
            if self.array[self.height-1][i][2] == border:
                sum_border += 1

        for i in range(self.height):
            if self.array[i][0][3] == border:
                sum_border += 1
            if self.array[i][self.width-1][1] == border:
                sum_border += 1

        # Inside the border
        for i in range(1, self.height-1):
            for j in range(1, self.width-1):
                if self.array[i][j][0] == self.array[i-1][j][2]:
                    self.bool_array[i][j][0] = True
                    self.bool_array[i-1][j][2] = True

                if self.array[i][j][1] == self.array[i][j+1][3]:
                    self.bool_array[i][j][1] = True
                    self.bool_array[i][j+1][3] = True

                if self.array[i][j][2] == self.array[i+1][j][0]:
                    self.bool_array[i][j][2] = True
                    self.bool_array[i+1][j][0] = True

                if self.array[i][j][3] == self.array[i][j-1][1]:
                    self.bool_array[i][j][3] = True
                    self.bool_array[i][j-1][1] = True
                
        # On the border
        for i in range(self.width-1):
            if self.array[0][i][1] == self.array[0][i+1][3]:
                self.bool_array[0][i][1] = True
                self.bool_array[0][i+1][3] = True

            if self.array[self.height-1][i][1] == self.array[self.height-1][i+1][3]:
                self.bool_array[self.height-1][i][1] = True
                self.bool_array[self.height-1][i+1][3] = True

        for i in range(self.height-1):
            if self.array[i][0][2] == self.array[i+1][0][0]:
                self.bool_array[i][0][2] = True
                self.bool_array[i+1][0][0] = True

            if self.array[i][self.width-1][2] == self.array[i+1][self.width-1][0]:
                self.bool_array[i][self.width-1][2] = True
                self.bool_array[i+1][self.width-1][0] = True

        for i in range(self.height):
            for j in range(self.width):
                for k in range(self.squares):
                    if self.bool_array[i][j][k]:
                        suma += 1
        
        if squares:
            print(self.bool_array)
            return suma//2
        
        return suma+sum_border