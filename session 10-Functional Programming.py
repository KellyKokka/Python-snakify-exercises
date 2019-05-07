#Session 10
#List_of_combined_pairs

X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]
for x in X:
    for y in Y:
        if x<y:
            print(x,y)

#Squared_Mapping

X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]
def square(X):
    for i in range(len(X)):
        X[i]=X[i]*X[i]
    return X    
it =zip(square(X),Y)
for x in it: print(x[0], x[1])

#Matrix_Comprehension

def create_matrix(m,n):
    M =[[i+j for i in range(n)] for j in range(m)]
    return M

#NO modifications below this line
inp = input().split()
m,n = int(inp[0]), int(inp[1])
M = create_matrix(m,n)
print(M)

#Higher_Order_Functions

def stringify(f):
    #implement this higher order function
    def new(X):
        Y=""
        for x in X:
            Y+=f(x)
        return Y
    return new 

#NO changes below this line
import sys
s = input()
complete_in = sys.stdin.read()
exec(complete_in)
F = stringify(f)
print(F(s))
