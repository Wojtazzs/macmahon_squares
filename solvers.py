import math
from numpy.random import rand
from squares import MacMahonSquares
import copy
from random import randint

# simulated annealing algorithm
def simulated_annealing(
        Function, 
        iter: int, 
        temp: int
        ):
    
    x = MacMahonSquares()
    x.randomize()
    y = x.sum_square()
    curr_x = copy.deepcopy(x)
    curr_y = y

    for i in range(iter):

        test_x = copy.deepcopy(curr_x)
        test_x.swap_random()
        test_y = test_x.sum_square()

        if test_y > y:
            x = copy.deepcopy(test_x)
            y = test_y
            continue
        
        diff = test_y - curr_y
        t = temp / float(i + 1)

        try:
            res = math.e ** (-diff / t)
        except OverflowError:
            res = 1

        if diff > 0 or rand() > res:
            curr_x = copy.deepcopy(test_x)
            curr_y = test_y

    return x, y


def tabu_search(
        x,
        iter: int, 
        tabu_size: int,
        ):
    
    def random_coord():
        i = randint(0, x.height-1)
        j = randint(0, x.width-1)
        k = randint(0, x.squares-1)
        return [i, j, k]


    coord = random_coord()
    y = x.sum_square()

    x_candidate = copy.deepcopy(x)

    tabulist = []
    neighbours = []

    for _ in range(5):
        neighbours.append(random_coord())

    for i in range(iter):
        
        for j, neighbour in enumerate(neighbours):
            test = random_coord()

            while test in neighbours or test in tabulist:
                test = random_coord()
            
            neighbours[j] = test

        for neighbour in neighbours:
            x_test = copy.deepcopy(x_candidate)
            x_test.swap(coord, neighbour)

            if x_test.sum_square() >= x_candidate.sum_square():   
                x_candidate = copy.deepcopy(x_test)
                coord = neighbour

        if x_candidate.sum_square() > x.sum_square():
            x = copy.deepcopy(x_candidate)

        tabulist.append(coord)
        
        if len(tabulist) > tabu_size:
            tabulist.pop(0)

    return x, y