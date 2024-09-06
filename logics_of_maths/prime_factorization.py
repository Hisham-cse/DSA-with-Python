def isPrime(n):
    if n==1 or n==0:
        return False
    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True
def Prime_factor(n):
    for i in range(2,n+1):
        if isPrime(i):
            x=i
            while n%x==0:
                print(i)
                x=x*i 
n=int(input())
print(Prime_factor(n))