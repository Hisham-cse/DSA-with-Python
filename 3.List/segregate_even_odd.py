def separate(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
l=[10,20,3,5]
print(separate(l))
even,odd=separate(l)

print(even)
print(odd)