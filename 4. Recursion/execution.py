# simple execution
def fun(n):
    if n<=0:
        return
    print("GFG")
    fun(n-1)
n=int(input("Enter a number: "))
fun(n)