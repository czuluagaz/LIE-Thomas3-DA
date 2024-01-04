import re

my_string = "let's write REGEx"
print(re.findall(r"\w+", my_string))
