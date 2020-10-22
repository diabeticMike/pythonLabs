import math

# 1
print('Введіть a,b,c')
a = float(input())
b = float(input())
c = float(input())
p = (a+b+c)/2
print(math.sqrt(p*(p-a)*(p-b)*(p-c)))

# 2.1
print('Введіть x,y')
x = float(input())
y = float(input())
if math.fabs(x*y) < 1 and x < 0:
    print(1)
    print((x+y)/math.exp(x*y))
elif 2 < x and y <= 0:
    print(2)
    print(-pow(math.log(math.exp(1),x), 2))
elif 0 < y and 0 <= x and x <= 2:
    print(3)
    print(math.log10(math.sqrt(y)))

# 2.2.1
print('Введіть число')
a = int(input())
if a < 5:
    print('Чисто менше 5')
else:
    if a % 5 != 0:
        print('Для ділення без остачі на 5 вам потрібно додати ', 5 - a % 5)
if a < 10:
    print('Чисто менше 10')
else:
    if a % 10 != 0:
        print('Для ділення без остачі на 10 вам потрібно додати ', 10 - a % 10)

# 2.2.2
def Z(x,y):
    print((x*y)/(x-y))

x = float(input())
y = float(input())
Z(x,y)