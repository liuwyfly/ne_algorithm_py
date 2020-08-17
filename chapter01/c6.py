"""
06 单身狗配对
源自括号配对 例如：()(())
"""

# @Author: Anderson
# @Date:   2018-08-11 17:26:45
# @Last Modified by:   Anderson
# @Last Modified time: 2018-08-17 14:33:38
s = input()

stack = []
can_match =True
for item in s:
    if item == 'm':
        stack.append('m')
    else:
        if len(stack)==0:
            can_match = False
            break
        else:
            stack.pop()
if len(stack)>0:
    can_match = False
print(can_match)
