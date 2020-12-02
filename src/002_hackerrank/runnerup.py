if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    print(arr.remove(max(arr)))
    print(max(arr))
    