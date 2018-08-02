# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(x,y,z):
    if bigger(x,y) == bigger(x,z):
        if y>z:
            return y
        return z
    if bigger(y,x) == bigger(y,z):
        if x>z:
            return x
        return z
    if bigger(z,x) == bigger(z,y):
        if x>y:
            return x
        return y

print(median(2,1,3))
#>>> 2

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7
