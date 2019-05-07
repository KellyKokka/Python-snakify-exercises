#Session 3
#Lists

#Even lists
a=[]
s=input()
a.append(s)
a = s.split()
for i in range(len(a)):
    if i%2==0:
       print(a[i])

#Even elements

a = input().split()
for i in a:
    if int(i)%2==0:
       print(int(i))

#Greater that previous
       
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        print(a[i])

#Neighbours of the same sign

 a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i]*a[i-1]>0:
        print(a[i-1],a[i])
        break

#Greater than neighbours

j=0
a = [int(i) for i in input().split()]
for i in range(1, len(a)-1):
    if a[i] > a[i-1] and a[i]>a[i+1]:
        j+=1
print(j)

#The largest element

a = [int(i) for i in input().split()]
max=a[0]
i=0
j=0
for elem in a:
    if elem>max:
        max=elem
        i=j
    j=j+1    
print(max,i)

#The number of distinct elements

a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)

#Swap neighbours

a = [int(i) for i in input().split()]
for i in range(0, len(a)-1,2):
    d=a[i]
    if len(a)%2==0:
       a[i]=a[i+1]
       a[i+1]=d
    else:
        a[i]=a[i+1]
        a[i+1]=d
        a[-1]=a[-1]
for i in a:
    print(i)

#Swap min and max

 index_of_max = 0
index_of_min=0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i]<a[index_of_min]:
        index_of_min=i
d=a[index_of_min]
a[index_of_min]=a[index_of_max]
a[index_of_max]=d
for i in a:
    print(i)

#Strings
    
#Slices

a=input()
print(a[2])
print(a[-2])
print(a[:5])
print(a[:len(a)-2])
sum=""
total=""
for i in range(len(a)):
    if i%2==0:
       sum+=a[i]
    else:
        total+=a[i]
print(sum)
print(total)
all=""
k=""
for i in range(-1,-len(a)-1,-1):
    all+=a[i]
for i in range(-1,-len(a)-1,-2):    
        k+=a[i]
print(all)
print(k)
print(len(a))

#The number of words

print(input().count(' ') + 1)

#The first and the last occurence

a=input()
if a.count('f')==1:
    print(a.find('f'))
elif a.count('f') >= 2:
    print(a.find('f'), a.rfind('f'))

#Reverse the fragment

a=input()
c=a.count("h")
tot=""
if int(c)>=2:
    start=a.find("h")
    end=a.rfind("h")
    a1=a[:int(start)]
    a2=a[int(end):]
    for i in range(int(end),int(start),-1):
        tot+=a[i]
print(a1+tot+a2)

#Sets

#The number of distinct numbers

a=[int(i) for i in input().split()]
print(len(set(a)))

#The number of equal numbers

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
tot=set(a)&set(b)
print(len(set(tot)))

#The intersection of sets

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
tot=set(a)&set(b)
tot_list=list(tot)
tot_list.sort()
for i in tot_list:
    print(i)

#Cubes

def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])
N, M = [int(s) for s in input().split()]
A_colors, B_colors = set(), set()
for i in range(N):
    A_colors.add(int(input()))
for i in range(M):
    B_colors.add(int(input()))
print_set(A_colors & B_colors)
print_set(A_colors - B_colors)
print_set(B_colors - A_colors)

#Guess the number

n =int(input())
allpossibles=set(range(1, n + 1))
possibles=allpossibles
while True:
    guess=input()
    if guess=='HELP':
        break
    guess={int(x) for x in guess.split()}
    answer=input()
    if answer=='YES':
        possibles&=guess
    else:
        possibles&=allpossibles-guess
print(' '.join([str(x) for x in sorted(possibles)]))

#Dictionaries

#Number of occurences

dictio={}
for word in input().split():
    dictio[word] = dictio.get(word, 0) + 1
    print(dictio[word] - 1)

#Dictionary of synonyms

n=int(input())
dictio={}
i=1
while i<=n:
    key,value=input().split()
    dictio[key]=value
    i+=1
word=input()
for k,v in dictio.items():
    if v==word:
        print(k)
    elif k==word:
        print(v)

#Access rights

OPERATION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}
f_perm={}
for i in range(int(input())):
    file,*permissions=input().split()
    f_perm[file] = set(permissions)
for i in range(int(input())):
    operation, file = input().split()
    if OPERATION_PERMISSION[operation] in f_perm[file]:
        print('OK')
    else:
        print('Access denied')

#Frequency analysis

from collections import Counter
words=[]
for _ in range(int(input())):
    words.extend(input().split())
counter=Counter(words)
pairs=[(-pair[1], pair[0]) for pair in counter.most_common()]
words=[pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

