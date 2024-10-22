def fact(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*fact(n-1)
if __name__=='__main__':

    print(fact(0))

# def fact(n):
#     res=1
#     for i in range(2,n+1):
#         res=res*i
#     return res





# if __name__=='__main__':
#     print(fact(-1))