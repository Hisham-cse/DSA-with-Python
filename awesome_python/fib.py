def fib(N):
    if N==0:return 0
    if N==1:return 1
    n1,n2=0,1
    for i in range(2,N+1):
        sum=n1+n2
        n1=n2
        n2=sum
    return n2
n=int(input("Enter a Number: "))
print(fib(n))