import os 

def disk_usage(path):

    total = os.path.getsize(path)

    if os.path.isdir(path):
        for fileName in os.listdir(path):
            childPath = os.path.join(path,fileName)
            total  += disk_usage(childPath)
    print(total,path)
    return total
