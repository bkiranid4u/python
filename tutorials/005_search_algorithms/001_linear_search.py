""" 
Linear Search
 """


def search(arr, item):

    for i in range(len(arr)):

        if arr[i] == item:
            return i

    return -1


print(search([1, 2, 3, 4, 5, 6, 7], 9))
print(search([1, 2, 3, 4, 5, 6, 7], 1))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def search_improved(arr, item):

    length = len(arr)

    right = length - 1

    for left in range(0, right, 1):

        if item == arr[right]:
            print("Found by right side")
            return right

        if item == arr[left]:
            print("Found by Left side")
            return left
        right = right - 1

    return -1


print(search_improved([1, 2, 3, 4, 5, 6, 7], 7))
print(search_improved([1, 2, 3, 4, 5, 6, 7], 2))
