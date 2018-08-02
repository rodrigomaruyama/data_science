# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def check_length(p):
        for i in range(0,len(p)):
            if not len(p[i]) == len(p):
                return False
            else:
                return True


def symmetric(list):
    if not list == []:
        if check_length(list):
            a = 0
            for i in range(0,len(list[0])):
                for j in range(0,len(list[0])):
                    if list[i][j] == list[j][i]:
                        a += 1
                        if a == len(list)**2:
                            return True
                    else:
                        return False
        else:
            return False
    else:
        return True


print symmetric([[1, 2, 3],[2, 3, 4],[3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],["dog", "dog", "fish"],["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],["dog", "dog", "dog"],["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],[2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],[2, 3, 4, 5],[3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],[2,3,1]])
#>>> False

print symmetric([[1,2,3]])
#>>> False
