Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=input("Enter a number")
Enter a number 34
>>> n=int(n)
>>> if n%2==0:
...     print("No is even")
...     else:
...         
SyntaxError: invalid syntax
>>> else
SyntaxError: invalid syntax
>>> print("No is odd")
No is odd
>>> indian=["a","b","c"]
>>> italian=["a","b","c"]
>>> french=["a","b","c"]
>>> indian=["d","e","f"]
>>> italian=["p","q","r"]
>>> french=["t","u","v"]
>>> dish=input("Enter a dish")
Enter a dish a
>>> if dish is indian:
...     print(f"{dish}is indian")
... elif dish is italian:
...     print(f"{dish}is italian")
... if dish is french:
...     print(f"{dish}is french")
...     
SyntaxError: invalid syntax
>>> elif dish is french:
...     print(f"{dish}is french")
...     
SyntaxError: invalid syntax
>>> else:
...     
SyntaxError: invalid syntax
age=int(input("Enter age :"))
Enter age :19
if age>=18:
    print("Eligible")
   else:
       
SyntaxError: unindent does not match any outer indentation level
for i in range(10)
SyntaxError: expected ':'
for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9


for i in range(11)
SyntaxError: expected ':'
for i in range(11):
    if i%2==0:
        continue
    print(i)

    
1
3
5
7
9


key="chair"
ser=["a","b","chair","d"]
for loc in ser:
    if loc==key:
        print("Key found at :", loc)
        break
    else:
        print("Key not found at :", loc)
        print("end")

        
Key not found at : a
end
Key not found at : b
end
Key found at : chair


exp=[1,2,3,4]
t=0
for i in range(len(exp))
SyntaxError: expected ':'
for i in range(len(exp)):
    exp=exp[i]
    print(f'Month{i+1} , Expense :{exp}')
    t+=exp
    print("Total expense :", t)

    
Month1 , Expense :1
Total expense : 1
Traceback (most recent call last):
  File "<pyshell#58>", line 2, in <module>
    exp=exp[i]
TypeError: 'int' object is not subscriptable


exp=[1,2,3,4]
t=0
for i in range(len(exp)):
    print(f'Month{i+1} , Expense :{exp[i]}')
    t+=exp[i]
    print("Total expense :", t)
    
SyntaxError: multiple statements found while compiling a single statement

res=["h","t","t","h","t","h","h","t","t","t"]
c=0
for i in res:
    if i=="h":
     c+=1
     print("Head :", c)

     
Head : 1
Head : 2
Head : 3
Head : 4


#sq of all nos from 1 to 10 except even nos
for i in range(11):
    if i%2==0:
        continue
    print(i*i)

    
1
9
25
49
81


exp=[2340,2500,2100,3100,2980]
e=input("Enter exp :")
Enter exp :2
e=int(e)
month =-1
for i in range(len(exp)):
    if e==exp
    
SyntaxError: expected ':'
if e==exp:
    month=i
    break
SyntaxError: 'break' outside loop


#pattern
for i in range(1,6):
    s=''
    for j in range(i):
        s+='*'
        print(s)

        
*
*
**
*
**
***
*
**
***
****
*
**
***
****
*****


def vol_c(rad,ht)
SyntaxError: expected ':'
def vol_c(rad,ht):
    print("radius :", rad)
    print("height :", ht)
    v=3.14 * (rad * rad) * ht
    return v
r=5
SyntaxError: invalid syntax
print(vol_c(rad=5,ht=10))
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print(vol_c(rad=5,ht=10))
NameError: name 'vol_c' is not defined

def vol_c(rad,ht):
    print("radius :", rad)
    print("height :", ht)
    v=3.14 * (rad ** 2) * ht
    return v
r=5
SyntaxError: invalid syntax

import math
dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

math.log10(1000)
3.0
dir(calendar)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    dir(calendar)
NameError: name 'calendar' is not defined. Did you forget to import 'calendar'?
import calendar
dir(calendar)
['APRIL', 'AUGUST', 'Calendar', 'DECEMBER', 'Day', 'EPOCH', 'FEBRUARY', 'FRIDAY', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'IntEnum', 'JANUARY', 'JULY', 'JUNE', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MARCH', 'MAY', 'MONDAY', 'Month', 'NOVEMBER', 'OCTOBER', 'SATURDAY', 'SEPTEMBER', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__getattr__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_get_default_locale', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'global_enum', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'warnings', 'week', 'weekday', 'weekheader']

july=calendar.month(2024,7)
print(july)
     July 2024
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

august=calendar.month(2024,8)
print(august)
SyntaxError: multiple statements found while compiling a single statement
august=calendar.month(2024,8)
print(august)
    August 2024
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

