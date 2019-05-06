#Session 5

#Recursive sum

def rec_sum(x):
    if x==1:
        return 1
    else:
        if x>0:
           result=x+rec_sum(x-1)
           return result
n=int(input())
print(rec_sum(n))

#Recursive Exponentiation

def power(x,n):
    if n==0:return 1
    if n==1:
        return x
    elif n>1:    
       result=x*power(x,n-1)
       return result
a=float(input())
n=int(input())
print(power(a,n))

#Recursive max

def maxel(lst):
  if len(lst) == 1:
    return lst[0]
  else:
    max = maxel(lst[1:])
    if lst[0] > max:
      return lst[0]
    else:
      return max
a=[int(s) for s in input().split()]
print(maxel(a))

#Print all strings of given length containing 0 or 1

def print_01_strings(k,s,n):
    if k==n:
        print(s)
    else:
        print_01_strings(k+1,s+'0',n)
        print_01_strings(k+1,s+'1',n)
print_01_strings(0,'',int(input()))


