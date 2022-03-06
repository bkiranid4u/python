""" 
    Reverse the file using the stack
"""
from ArrayStack import ArrayStack


def reverse_file(fileName):

    fileStack = ArrayStack()
    original = open(fileName)

    for line in original:
        line.strip("\n")
        fileStack.push(line)
    original.close()

    output = open(fileName, 'w')

    while not fileStack.is_empty():
        line = fileStack.pop() + '\n'
        print(line)
        output.write(line)
    output.flush()
    output.close()


reverse_file('src/003_data_structures/stacks/file.txt')
