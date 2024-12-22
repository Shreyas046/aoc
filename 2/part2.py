import copy
ans = 0

with open("input.txt","r") as f:
    s = f.read()

# s = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

lines = s.split('\n')

def is_level_safe(line) -> bool:
    safe  = all(i < j for i, j in zip(line, line[1:])) or all(i > j for i, j in zip(line, line[1:])) 

    for i,j in zip(line,line[1:]):
        if abs(j-i) > 3 or abs(j-i) < 1:
            safe = False
    
    return safe

for line in lines:
    line = [int(i) for i in line.split(' ')]

    safe = is_level_safe(line)
    
    for i in range(len(line)):
        temp = copy.deepcopy(line)
        temp.pop(i)

        if is_level_safe(temp):
            safe = True
            break
    
    if safe:
        ans += 1


print(ans)