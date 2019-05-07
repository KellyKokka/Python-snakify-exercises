#Session 4

#Matrix Maximum Index Function

def matrix_max_index(A,m,n):
    best_i, best_j = 0, 0
    curr_max = A[0][0]
    for i in range(m):
       for j in range(n):
          if A[i][j] > curr_max:
             curr_max = A[i][j]
             best_i, best_j = i, j
    return best_i,best_j
nums =input().split() 
m = int(nums[0]) 
n = int(nums[1]) 
M = list() 
for i in range(0,m): 
    current_row_strings = input().split() 
    M.append([]) 
    for j in range(0,n): 
       M[i].append(int(current_row_strings[j])) 
(i,j) = matrix_max_index(M, m, n) 
print(i,j)

#Swap Columns Function

def swap_columns(A,m,n,i,j):
    for k in range(len(A)):
        A[k][i], A[k][j] = A[k][j], A[k][i]
nums =input().split() 
m = int(nums[0]) 
n = int(nums[1]) 
M = list() 
for i in range(0,m): 
     current_row_strings=input().split() 
     M.append([]) 
     for j in range(0,n): 
       M[i].append(int(current_row_strings[j])) 
nums =input().split() 
i = int(nums[0]) 
j = int(nums[1]) 
swap_columns(M, m, n, i, j) 
for i in range(0,m): 
  for j in range(0,n): 
    if j < n-1: 
       print(M[i][j], end = ' ') 
    else: 
       print(M[i][j], end = '') 
       if i < m-1: 
         print()

#Matrix Scaling Functions

def scale_matrix(M, m, n, c): 
    import copy
    B=copy.deepcopy(M)
    for i in range(m):
       for j in range(n):
          B[i][j] *= c
    return B
def print_matrix(M, m, n): 
   for i in range(0,m): 
      for j in range(0,n): 
        if j < n-1: 
           print(M[i][j], end = ' ') 
        else: 
           print(M[i][j], end = '') 
           if i < m-1: 
              print() 
nums =input().split() 
m = int(nums[0]) 
n = int(nums[1]) 
M = list() 
for i in range(0,m): 
    current_row_strings = input().split() 
    M.append([]) 
    for j in range(0,n): 
        M[i].append(int(current_row_strings[j])) 
c =int(input())
N = scale_matrix(M, m, n, c) 
print_matrix(N, m, n) 
print()
print_matrix(M, m, n)


         
