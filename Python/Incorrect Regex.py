import re

T = int(raw_input())
for i in range(T):
    try:
        re.compile(raw_input())
        print True
    except:
        print False
