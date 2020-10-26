import math

# 1
# a
x = -1.0
while -1 <= x and x <= 1:
    print(x, ": ",(2*math.pow(math.sin(x),3)) / (3*math.fabs(x)+1))
    x += 0.25
print()

# b
x = -2.5
n = 0
while x >= -2.5 and n < 6:
    print(n, ": ",(2*math.pow(math.sin(x),3)) / (3*math.fabs(x)+1))
    x += 0.25
    n+=1

# 2
try:
    n = int(input("Enter n >= 7\n"))
    if n < 7:
        print("n need to be >= 7")
    else:
        for v in range(100, 999):
            if v % 2 == 0 and v % n == 0:
                print(v)
except:
    print("n need to be int")

