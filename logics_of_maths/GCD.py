# def GCD(a,b):
#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#     return a

# if __name__=='__main__':
#     print(GCD(12,15))
    

    #    or 

def GCD(a,b):
    if b==0:return a
    return GCD(b,a%b)


if __name__=='__main__':
    print(GCD(12,15))