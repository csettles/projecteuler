# find the pythagorean triplet for which a + b + c = 1000
# a**2 + b**2 = c**2

ls = []

for c in range(1000):
    x1 = 1000 - c
    for b in range(x1):
        a = x1 - b
        if (a**2 + b**2 == c**2) and a*b*c != 0:
            ls.append(a)
            ls.append(b)
            ls.append(c)

# convert to a set and then back to list to remove duplicates
print(list(set(ls)))

ans = 1
for i in ls:
    ans *= i

print(ans)
