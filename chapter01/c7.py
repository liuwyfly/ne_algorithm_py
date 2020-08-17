"""
07 单身狗配对2
"""

# @Author: Anderson
# @Date:   2018-08-11 17:26:45
# @Last Modified by:   Anderson
# @Last Modified time: 2018-08-17 16:26:44
s = input()

s_list = s.split(' ')
stack = []
can_match =True
for item in s_list:
    if item[0] == 'm':
        stack.append(item)
    else:
        if len(stack) == 0:
            can_match = False
            break
        else:
            if stack[-1][1] == item[1]:
                stack.pop()

if len(stack) > 0:
    can_match = False
print(can_match)
