"""
共同分担
"""


def solve(index, current_a_weight):
    global min_diff
    if index == 0:
        pack_a = current_a_weight +  items[0]
        pack_b = total_weight - pack_a
        diff = abs(pack_a - pack_b)
        if diff < min_diff:
            min_diff = diff

        pack_a = current_a_weight
        pack_b = total_weight - pack_a
        diff = abs(pack_a - pack_b)
        if diff < min_diff:
            min_diff = diff
    else:
        solve(index - 1, current_a_weight + items[index])
        solve(index - 1, current_a_weight)


s = input()
s_list = s.split(' ')
items = [int(i) for i in s_list]
total_weight = sum(items)
min_diff = total_weight
solve(len(items) - 1, 0)
print(min_diff)
