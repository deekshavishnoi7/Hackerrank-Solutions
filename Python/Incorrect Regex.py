import re

n = int(input().strip())

for _ in range(n):
    regex = input().strip()
    try:
        re.compile(regex)
        print("True")
    except re.error:
        print("False")
