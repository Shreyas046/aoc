ans = res = 0
with open("input.txt","r") as f:
    s = f.read()

# s = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

left , right = [], []
for i in s.split('\n'):
    left.append(int(i.split('   ')[0]))
    right.append(int(i.split('   ')[1]))

count = {}

for i in range(len(right)):
    if right[i] in count:
        count[right[i]] += 1
    else:
        count[right[i]] = 1

for i in range(len(left)):
    if left[i] in count:
        ans += left[i] * count[left[i]]

print(ans)