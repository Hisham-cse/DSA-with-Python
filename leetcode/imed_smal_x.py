# Find Immediate Smaller Than X
# Input: 1
# N = 5
# arr[] = {4 67 13 12 15}
# X = 16
# Input:2
# N = 5
# arr[] = {1 2 3 4 5}
# X = 1
# Output: -1

class Solution:
    def immediateSmaller(self,arr,n,x):
        #return required ans
        immediate_Smaller = -1
        for i in range(n):
            if x>arr[i]:
                immediate_Smaller=max(immediate_Smaller,arr[i])
        return immediate_Smaller
x=int(input("Enter the value"))
l=[7,2,3,4,5]
n=len(l)
ob=Solution()
print(ob.immediateSmaller(l,n,x))