def isPal(n):
    rev=0
    temp=n
    while temp!=0:
        id=temp%10
        rev=rev*10+id
        temp=temp//10
    return n==rev



if __name__=='__main__':
    n=int(input("Enter a number: "))
    print(isPal(n))

