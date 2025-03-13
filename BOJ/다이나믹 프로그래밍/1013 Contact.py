# 1013 Contact

# (100+1+ | 01)+

# 파이썬에서 정규식 사용하는 방법
# import re
# reg = re.compile('정규식')
# result = reg.match(text) 또는 reg.fullmatch(text) -> fullmatch는 모든 문자열이 일치해야 하며 match는 문자열중 일부만 일치해도 됨

"""
10010111
011000100110001
0110001011001

NO
NO
YES
"""

import re

for i in range(int(input())):
    code = input()
    reg = re.compile('(100+1+|01)+')
    isMatch = reg.fullmatch(code)

    if isMatch:
        print('YES')
    else:
        print('NO')
