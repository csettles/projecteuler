# find the 10,001st prime number

rng = list(range(0, 200000))
ans = []
count = 0


def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    maximum = n**0.5+1
    i = 3
    while i <= maximum:
        if n % i == 0:
            return False
        i += 2
    return True


def check_count(n):
    if count == 10002:
        return True

for i in rng:
    if isprime(i):
        ans.append(i)
        count += 1
        if check_count(i):
            break
    else:
        continue

print(max(ans))
