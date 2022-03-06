"""  """


def fibonacci(n):
    if n <= 1:
        print(0)
        print(n)
        return (n, 0)
    else:
        (a, b) = fibonacci(n-1)
        print(a+b)
        return (a+b, a)


print(fibonacci(6))


def fibanocci1(nterms):
# Program to display the Fibonacci sequence up to n-th term


    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1


fibanocci1((10))


