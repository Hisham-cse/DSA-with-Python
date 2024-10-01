class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        #code here
        count=0
        for i in range(len(arr)):
            if x>arr[i]:
                count+=1
        return count
ob=Solution()
print(ob.smallerThanX([1,2,3,4,5],5,3))    