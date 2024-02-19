def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def prime(n):
    ans=True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            ans=False
    return ans

def is_exp_5():
    while n >= 5:
        n //= 5
    return n == 1
