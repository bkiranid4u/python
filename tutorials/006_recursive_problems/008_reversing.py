

def reverse_recursive(s,start,end):
    # reverse the given list 

    # Base condition
    if start < end -1:
        s[start],s[end-1]=s[end-1],s[start]
        reverse_recursive(s, start+1, end-1)
    return s

print(reverse_recursive([x for x in range(1, 11)], 0, 10))

def reverse(s,start,end):

    while start < end:
        s[start], s[end-1] = s[end-1], s[start]
        start +=1
        end -=1
    return s


print(reverse([x for x in range(1, 11)], 0, 10))
