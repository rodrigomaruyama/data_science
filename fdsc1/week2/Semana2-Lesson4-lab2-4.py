# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

def check_length(p):
        for i in range(0,len(p)):
            if not len(p[i]) == len(p):
                return False
            else:
                return True


def is_identity_matrix(matrix):
    a = 0
    b = 0
    if check_length(matrix):
        count_a = 0
        count_b = 0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                if i==j:
                    if matrix[i][j] == 1:
                        count_a += 1
                        if count_a == len(matrix):
                            a = 1
                else:
                    if matrix[i][j] == 0:
                        count_b += 1
                        if count_b == len(matrix)**2 - len(matrix):
                            b = 1
                    else:
                        b = 0
    else:
        a == 0
    if a == 1 and b == 1:
        return True
    else:
        return False





# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False

           
