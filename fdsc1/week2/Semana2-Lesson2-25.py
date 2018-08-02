# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.

def measure_udacity(list):
    count = 0
    i=0
    while i < len(list):
        if list[i].find('U') == 0:
            count = count + 1
            i = i +1
        else:
            i = i +1
    return count



print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2
