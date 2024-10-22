"""
    Check if a given number or string is a palindrome.

    A palindrome is a sequence that reads the same backward as forward.

    Parameters:
    N (int or str): The number or string to check for palindrome properties.

    Returns:
    int: Returns 1 if the input is a palindrome, otherwise returns 0.
    """
def ispali(N):
    N=str(N)
    start = 0
    end =len(N)-1
    def Pali(N,start,end):
        if start==end:
            return 1
        elif N[start]==N[end]:
            return Pali(N,start+1,end-1)
        else:
            return 0
    return Pali(N,start,end)
a=ispali(101)
print(a)
a=ispali(100)
print(a)