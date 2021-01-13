line = str(raw_input())

d = {}
for t in line.split(' '):
    if t in d:
        d[t] += 1
    else:
        d[t] = 1

for k, v in d.items():
    print('{} {}'.format(k, v))