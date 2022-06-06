nl = int(input())
p = []
for i in range(nl):
    p.append(input())
p = "".join(p)
nv = 0
nc = 0
for c in p:
    if c in 'aeiouAEIOU':
        nv += 1
    elif c in 'bBcBdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ':
        nc += 1
print('Number of vowels:', nv)
print('Number of consonant:', nc)
