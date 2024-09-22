def insertAtEnd(arr,sizeOfArray,element):
    ##Your code here
    for i in range(sizeOfArray):
        if i==sizeOfArray:
            arr.insert(element)
    return arr
print(insertAtEnd([1,2,3,4,5],6,90))