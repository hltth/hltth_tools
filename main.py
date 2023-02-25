import math
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for f in range(10):
                    num = a*10000+b*1000+c*100+d*10+f
                    num2 = (a + b + c+ d + f) * math.pow((math.pow(a,2) +  math.pow(b,2) +  math.pow(c,2)  +  math.pow(d,2) + math.pow(f,2)),2)
                    if num == num2:
                        print(num)
