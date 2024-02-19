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


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def automat(phrase):
    if phrase == "Будь ласка":
        print("А ви Циско поробили?")
    else:
        return None

def IsEven(n):
    if n%2==0: return True
    else: return False

def Is_O(string):
    if string == "O":
        return True
    else:
        return False
