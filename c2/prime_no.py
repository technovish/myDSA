
a=input("enter number:")
x=int(a)

def is_prime(x):
    if x <= 1:
        return False
    a = 0
    for n in range(1, x):
        if x % n == 0:
            a += 1
            print(a)
        if a >= 2:
            break
    else:
        return True
    return False

i=is_prime(x)
print(i)