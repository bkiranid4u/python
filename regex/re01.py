import re

pattern = re.compile(r'\bfoo\b')
print(pattern.search("bar foo barfoo"))
