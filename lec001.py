def fib(n):

    if not (isinstance(n, int)):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

#time: 0(2^n)
#space: 0^n

if __name__ == "__main__":
    print(fib(30))

#the above solution is slow and inefficient for large n

#the modified version of the above solution is as follows:


    #we calculate the ith Fibonacci number from the previous two 
    #if it equals the target, return the target 

def fib_optimized(target, i_minus_1, i_minus_2, i): 
    fib_i = fib_i_minus_1 + fib_i_minus_2
    if i == target:
        return fib_i
    else:
        return fib_optimized(target, fib_i, i_minus_1, i + 1)
   

if __name__ == "__main__":
    print(fib_optimized(50))

