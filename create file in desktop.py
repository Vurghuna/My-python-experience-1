Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = open(":/Users/Vurgune Bagirova/Desktop/myfile.txt", "x")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a = open(":/Users/Vurgune Bagirova/Desktop/myfile.txt", "x")
OSError: [Errno 22] Invalid argument: ':/Users/Vurgune Bagirova/Desktop/myfile.txt'
>>> a
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> print("f", flush = True)
f
>>> f = open("C:/Users/Vurgune Bagirova/Desktop/myfile.txt", "x")
>>> f = open("C:/Users/Vurgune Bagirova/Desktop/myfile.txt", "x")