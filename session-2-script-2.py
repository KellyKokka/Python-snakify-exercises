def next_number(n):
    k = n+1
    return k

def pi():
    return 3.14

def print_double(n):
    print(n*2)


#functions calling other functions

def next_number_even(n):
    k = next_number(n)
    result = (k%2 == 0)
    return result

A = 10
C = next_number_even(A)
print(C)
