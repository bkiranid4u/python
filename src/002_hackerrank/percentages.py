if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = list()
    scores = list(student_marks.get(query_name))
    avg = sum(scores)/len(scores)
    precision = 4
    width = 4
    print("{avg}:{width}.{precision}".format(avg,width,precision))

