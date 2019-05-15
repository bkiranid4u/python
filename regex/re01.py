import re

pattern = re.compile(r'<HTML>')
print(pattern.match(" <HTML><Head></..>", re.))
