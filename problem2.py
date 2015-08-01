#fibonacci sum of even nums under four million
ls = [1, 2]
result = 0

while ls[-1] < 4000000:
    ind = len(ls)
    num = ls[ind-1] + ls[ind-2]
    ls.append(num)

for i in ls:
    if (i % 2) == 0:
        result += i

print(result)