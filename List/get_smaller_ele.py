def smaller_ele(l,x):
    lst=[]
    for i in l:
        if i<=x:
            lst.append(i)
        
    return lst


l=[10,20,30,40,50]
x=30
print(smaller_ele(l,x))