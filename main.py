import squares
import solvers
import copy

mc = squares.MacMahonSquares(4, 6, 3)

mc.randomize()
print()
mc.print()
print(f"Before annealing: {mc.sum_square(True)}")
print()
mc2 = copy.deepcopy(mc)
mc, y = solvers.simulated_annealing(mc, 10_000, 10)
#mc, y = solvers.tabu_search(mc, 100_000, 10)
mc.print()
print(f"Result of annealing: {mc.sum_square(True)}")
print()
mc2, y = solvers.tabu_search(mc2, 10_000, 10)
mc2.print()
print(f"Result of tabu search: {mc2.sum_square(True)}")
