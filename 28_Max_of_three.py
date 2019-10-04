# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using
# the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is
# some variables and if statements!\


# Function finding the largest of three numbers
#
# x, y, z - numbers to check
def max_of_three(x, y, z):
    num = x
    if y > num:
        num = y
    if z > num:
        num = z
    return num


if __name__ == "__main__":
    print(max_of_three(12, 7, 13))
