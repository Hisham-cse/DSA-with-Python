
def natural_number(N):
    """
    Calculate the sum of the first N natural numbers using [recursion](https://www.geeksforgeeks.org/recursion/).

    Parameters:
    N (int): The number up to which the sum of natural numbers is calculated. 
             It should be a non-negative integer.

    Returns:
    int: The sum of the first N natural numbers. If N is less than or equal to 1, returns 1.
    """
    if N <= 1:
        return 1
    return N + natural_number(N - 1)

   
    
n=10
a=natural_number(n)
print(a)