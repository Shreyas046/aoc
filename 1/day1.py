ans = res = 0
with open("input.txt","r") as f:
    s = f.read()

left , right = [], []
for i in s.split('\n'):
    left.append(int(i.split('   ')[0]))
    right.append(int(i.split('   ')[1]))

left.sort()
right.sort()

ans = sum([abs(left[i]- right[i]) for i in range(len(left))])
print(ans)