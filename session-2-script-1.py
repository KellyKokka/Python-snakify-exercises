Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Program control structures
>>> #iteration
>>> s = 'Hello'
>>> s += '!'
>>> print(s)
Hello!
>>> s += '!'
>>> s += '!'
>>> s += '!'
>>> s += '!'
>>> s += '!'
>>> print(s)
Hello!!!!!!
>>> n = int(input('How many times'))
How many times12
>>> #while loops
>>> m = 0
>>> while m < n:
	s+='!'
	m+=1

	
>>> print(s)
Hello!!!!!!!!!!!!!!!!!!
>>> s = 'Hello'
>>> for m in range(0,n):
	s+='!'

	
>>> print(s)
Hello!!!!!!!!!!!!
>>> #prompt the user to enter word after word. Stop when 'stop' was entered. Print how many words were entered before stop
>>> count = 0
>>> current_word = input('Enter a word: ')
Enter a word: first
>>> while current_word != 'stop':
	count+=1
	current_word = input('Enter a word: ')

	
Enter a word: second
Enter a word: third
Enter a word: fourth
Enter a word: stop
>>> print(count)
4
>>> #loop inside loop
>>> #for a given n, print a pyramid of numbers from 1 to n, e.g.
>>> #1
>>> #2 2
>>> #3 3 3
>>> n = 3
>>> for i in range(1, n+1):
	for j in range(1, i+1):
		print(i, end=' ')
	print()

	
1 
2 2 
3 3 3 
>>> #functions
>>> def next_number(n):
	k = n+1
	return k

>>> A = 10
>>> C = next_number(A)
>>> print(C)
11
>>> C = next_number(100)
>>> print(C)
101
>>> 
=================== RESTART: C:/popi/example-session-2.py ===================
>>> 
=================== RESTART: C:/popi/example-session-2.py ===================
3.14
>>> 
=================== RESTART: C:/popi/example-session-2.py ===================
False
>>> 
