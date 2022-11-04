Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1=3
>>> num2=5
>>> type(num1)
<class 'int'>
>>> type(num2)
<class 'int'>
>>> result=num1/num2
>>> result
0.6
>>> type(result)
<class 'float'>
>>> num1=10284,2
>>> num2=2
>>> result=num1/num2
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    result=num1/num2
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
>>> num1=10234.23
>>> num2=3231.1
>>> result=num1/num2
>>> result
3.1674135743245335
>>> num1+num2
13465.33
>>> num1="help"
>>> num2="me"
>>> num1+num2
'helpme'
>>> num1,num2
('help', 'me')
>>> print("num1","num2")
num1 num2
>>> myname="Vurghuna"
>>> mylastname="Baghirova"
>>> 