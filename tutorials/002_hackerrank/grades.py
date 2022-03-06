if __name__ == '__main__':
    students = list()
    for i in range(int(input())):
        name = input()
        score = float(input())
        student = list();
        student.append(name)
        student.append(score)
        students.append(student)
    grades = set()
    for name,score in students:
        if score not in grades:
            grades.add(score)
    scoreList = list(grades)
    scoreList.remove(min(scoreList))
    secondLowest = min(scoreList)
    filteredStudents = sorted([name for name,score in students if score == secondLowest])
    [print(name) for name in filteredStudents]