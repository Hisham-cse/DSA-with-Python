def fun1():
    print("fun1() Called")
def fun2():
    print("Before fun2()")
    fun1()
    print("After fun2()")
print("before fun2()")
fun2()
print("After fun2()")