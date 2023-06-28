""" This file will contain details about: Hamiltonian Cycle """

#Notes about Hamiltonian Cycle
#Does not matter if not every edge is visited
#Key idea is the we start at one vertex and end the same vertex
#A graph can have multiple Hamiltonian Cycles
#I will focus on backtracking (brute-forcing) 1 solution




if __name__ == "__main__":
    graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
    }

    a_solution = [0, 1, 3, 2, 0]