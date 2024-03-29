import math
def f(n):
    if n==1:
        return 1
    else :
        return n*math.factorial(n-1)    

k=int(input("숫자를 기입하세요"))
s=f(k)
print(s)
