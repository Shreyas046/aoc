ans = res = 0

with open("input.txt","r") as f:
    s = f.read()

# s = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

lines = s.split('\n')

for line in lines:
    line = [int(i) for i in line.split(' ')]
    res  = all(i < j for i, j in zip(line, line[1:])) or all(i > j for i, j in zip(line, line[1:])) 

    for i,j in zip(line,line[1:]):
        if j-i > 3 or i-j > 3:
            res = False

    if res:
        ans += 1


print(ans)