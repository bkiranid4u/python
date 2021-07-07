
def linear_sum(s,n):
    if n ==0:
        return 0
    else:
        return linear_sum(s,n-1) + s[n-1]

print(linear_sum([x for x in range(1,101)],50))
