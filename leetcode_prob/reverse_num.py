x = 21470
b=0
c = -1
y = 0
if x < 0:
    d = c*x
    print("if its -ve num ", d)
elif x > 0:
    d = x
    print("if its +ve num ", d)

while d:
    b = b*10 + d%10
    d = d // 10
    print("hi")
#print(b)
if x < 0:
    y = c*b
    print("if its -ve num ", y)
elif x > 0:
    print("if its +ve num ", b)

