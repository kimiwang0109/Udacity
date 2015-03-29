# Write a function solve_3SAT using the search-tree technique outlined
# below that takes as its input a 3-SAT instance (see Problem Set 2),
# applies pre-processing (see Problem Set 4), and then uses a search tree
# to find if the given instance has a satisfying assignment. Your function
# should return None if the given instance of 3SAT has no satisfying
# assignment and otherwise return a satisfying assignment.

# Take any clause that is not satisfied
# * If all variables have already been set, then there is no
#   possible solution anymore
# * Otherwise, branch into at most three cases where in each case a different
#   variable is set so that the clause becomes satisfied:
#  - The first variable is set so that clause becomes satisfied
#    (and we don't do anything with the other variables)
#  - The first variable is set so that clause does not becomes satisfied,
#    the second one is set so that it becomes satisfied and we don't do
#    anything with the third variable.
#  - The first and second variable are set so that the clause does not
#    become satisfied, the third one is set so that it does become satisfed.

# Note that any solution must fall into one of the above categories.
# Naturally, after having applied the pre-processing and also during the
# branching, some clauses will not contain three unassigned variables anymore
# and your program needs to account for that.

# You may write any additional functions you require to solve this problem.
from itertools import combinations

def sat_single(empty, cl):
    for ix in range(3):
        if (cl[ix] > 0 and empty[abs(cl[ix])-1] ==1) or (cl[ix]<0 and empty[abs(cl[ix])-1]==0):
            return True
    return False

def sat(empty, clauses):
    for cl in clauses:
        if sat_single(empty, cl) == False:
            return False
    return True
    

def solve_3SAT(num_variables, clauses):
    # Your code here
    flag = [0]
    for i in range(0,num_variables+1):
        base = range(num_variables)
        li = [list(tup) for tup in combinations(base, i)]
        #print li
        for l in li:
            empty = [0 for y in range(num_variables)]
            
            for x in l:
                empty[x] = 1
            if sat(empty, clauses):
                return flag+empty
    return None
clauses = [[11, 10, 9], [-14, -6, -17], [-7, -9, 12], [-4, 6, -7], [9, 7, 6], [18, 14, -15], [-3, 6, 12], [9, -18, 17], [-16, 6, 11], [15, -4, 11], [15, 4, 1], [4, -16, 5], [1, -15, 18], [-11, -2, 17], [-11, -17, 4], [-10, -15, 11], [-16, 8, -9], [9, 15, 17], [10, -4, 7], [-4, -12, -5], [11, -5, -3], [-11, -16, 1], [-14, -12, 7], [8, 15, 18], [1, 9, 5], [12, -7, 1], [-13, -8, 16], [18, -6, 17], [5, 12, -7], [-8, -11, 1], [3, 12, 15], [13, -3, 12], [13, -12, -1], [17, 3, -9], [-6, -10, 7], [5, 10, -3], [-4, -12, 10], [12, 4, 5], [4, 9, 17], [15, 5, -17], [6, -15, -8], [-12, 8, -2], [-16, 13, 14], [-5, 3, -18], [9, 8, -16], [-3, -5, 16], [-18, 12, -6], [18, -2, -10], [5, 16, 8], [17, -3, 15], [-15, -6, 3], [18, 4, -17], [14, -12, 5], [2, 11, 16], [-12, -9, -18], [17, -15, -14], [6, -16, 2], [-3, 14, -1], [12, 4, 6], [-10, -2, -11], [8, 3, 4], [5, 16, -2], [-6, 8, -15], [13, -3, -17], [4, -14, -9], [-1, -8, -6], [-10, 17, -15], [13, 2, -1], [-9, 8, -1], [-10, 9, 18], [7, -9, 16]]        
#clauses = [[18, 12, -10], [-19, 13, 5], [13, -15, -20], [4, -17, 15], [9, 8, -14], [11, -9, 15], [-1, -17, 4], [-16, -14, 13], [-17, 7, -11], [18, 3, -1], [-12, -10, 1], [-13, -10, 16], [16, -19, 13], [2, 7, 13], [3, 11, -10], [-6, -2, 19], [15, 8, -13], [-19, -13, 14], [-7, -6, 18], [-12, -2, -19], [9, -15, -4], [1, -6, -10], [-15, -7, 14], [-17, -3, 16], [12, 13, 16], [-10, -19, 9], [15, -1, 12], [-5, 4, 16], [18, 4, 3], [-18, -8, -12], [3, -5, -14], [15, -20, 2], [-4, -19, -20], [-15, 4, 20], [-2, 3, -5], [8, 7, 20], [-18, 13, -4], [14, 12, -4], [-2, 8, -13], [7, 12, -13], [-7, -4, 12], [17, -15, -13], [-9, -3, 17], [-9, -12, -19], [18, 17, -12], [-3, -14, 17], [-15, -4, 19], [-12, -1, 10], [-16, 19, 8], [-8, -15, 6], [-5, -9, -12], [-20, -15, 17], [-10, -18, -7], [-16, 6, -1], [-7, -20, -4], [-1, 13, 15], [15, 8, 17], [-9, -12, -16], [-13, 1, -12], [14, -9, -5], [2, -4, 6], [7, -19, 15], [13, 9, 17], [-7, 13, -12], [-10, 12, 8], [-14, -17, -5], [-3, 18, -17], [3, -9, -15], [9, 7, 14], [20, -13, 19], [-7, 13, -17], [9, -10, 12], [-1, 16, 20], [-4, -7, 1], [6, 1, 7], [-9, 19, -11], [-20, -18, -7], [-5, 14, 6], [-5, -19, -10], [18, 5, -15], [19, -7, 8], [17, -18, -14], [11, -13, 10], [11, 15, -7], [-7, 19, 8], [-1, 14, -5], [-4, -19, 3], [4, -20, -14], [20, 2, 3], [7, 15, 16], [1, 18, -17], [-13, 18, 20], [-4, -17, -2], [15, -3, 8], [18, -3, 20], [1, -8, 9], [5, 19, -8]]
print solve_3SAT(18,clauses)
def test():
    clauses = [[-2, -3, -1], [3, -2, 1], [-3, 2, 1],
               [2, -3, -1], [3, -2, 1], [3, -2, 1]]
    solutions = [[0, 0, 0, 0],
                 [0, 0, 1, 1],
                 [0, 1, 0, 0],
                 [0, 1, 1, 0],
                 [1, 0, 0, 0],
                 [1, 0, 1, 1],
                 [1, 1, 0, 0],
                 [1, 1, 1, 0]]
    assert solve_3SAT(3,clauses) in solutions

    clauses = [[2, 1, 3], [-2, -1, 3], [-2, 3, -1], [-2, -1, 3],
               [2, 3, 1], [-1, 3, -2], [-3, 2, 1], [1, -3, -2],
               [-2, -1, 3], [1, -2, -3], [-2, -1, 3], [-1, -2, -3],
               [3, -2, 1], [2, 1, 3], [-3, -1, 2], [-3, -2, 1],
               [-1, 3, -2], [1, 2, -3], [-3, -1, 2], [2, -1, 3]]
    assert solve_3SAT(3,clauses) == None
    print 'Tests passed'
test()