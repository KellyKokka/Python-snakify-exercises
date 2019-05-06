Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Hello world')
Hello world
>>> 
========================= RESTART: C:/popi/prog1.py =========================
Hello world
Hello again
>>> #simple datatypes
>>> type(40)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type(40.0)
<class 'float'>
>>> type('Hello world')
<class 'str'>
>>> type(True)
<class 'bool'>
>>> #simple expressions
>>> 40+2
42
>>> type(40+2)
<class 'int'>
>>> type(40+3.14)
<class 'float'>
>>> type(40/3)
<class 'float'>
>>> type(40//3)
<class 'int'>
>>> 40//3
13
>>> type(40%3)
<class 'int'>
>>> 2**3
8
>>> 'Hello'+' World'
'Hello World'
>>> 'Hello' + 2
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    'Hello' + 2
TypeError: must be str, not int
>>> 'Hello ' + str(2)
'Hello 2'
>>> 'Hello ' + str(3.14)
'Hello 3.14'
>>> '5' + 2
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    '5' + 2
TypeError: must be str, not int
>>> int('5') + 2
7
>>> int(3.14)
3
>>> #boolean expression
>>> True and False
False
>>> type(True and False)
<class 'bool'>
>>> not True
False
>>> 3 < 4
True
>>> 4 < 3
False
>>> 3 < 4 or 4 < 3
True
>>> 3 == 4
False
>>> 3==3
True
>>> #variables (input)
>>> n = 2
>>> type(n)
<class 'int'>
>>> n = 3
>>> m = 5
>>> n = m
>>> print(n)
5
>>> n = n + 1
>>> print(n)
6
>>> n += 1
>>> print(n)
7
>>> s = 'Hello world'
>>> type(s)
<class 'str'>
>>> s1 = s
>>> type(s1)
<class 'str'>
>>> s1
'Hello world'
>>> s = input('Enter name')
Enter nameJohn
>>> type(s)
<class 'str'>
>>> s
'John'
>>> n = 10
>>> m = 12
>>> n < m
True
>>> #print command
>>> n = 5
>>> print(n)
5
>>> print('Numer is equal to ')
Numer is equal to 
>>> print('Number is equal to', 5)
Number is equal to 5
>>> print('Number is equal to', 5, 'print somethning else')
Number is equal to 5 print somethning else
>>> print('Number is equal to', n, 'print somethning else')
Number is equal to 5 print somethning else
>>> n
5
>>> n = n+1
>>> n = n+1.1
>>> n
7.1
>>> 
