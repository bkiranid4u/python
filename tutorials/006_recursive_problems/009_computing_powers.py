

def compute_power(x,n):
    if n == 0:
        return 1
    else:
        return x * compute_power(x,n-1)

def power(x,n):
    if n ==0:
        return 1
    else:
        partial = power(x,n//2)
        result = partial * partial

        if n %2 !=0:
            return x * result
        else:
            return result

print(power(2,5))
print(compute_power(2, 5))
