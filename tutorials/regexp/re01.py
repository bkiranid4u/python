import re

pattern = re.compile(r'\bfoo\b')
print(pattern.search("bar foo barfoo"))

pattern = re.compile(r"(\w+) (\w+)")
iter=pattern.finditer("Hello World hola munda")
print(next(iter).groups())
for match in iter:
    print(match)


