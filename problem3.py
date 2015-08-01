# find the  largest prime factor of the number 600851475143
import functools

ans_list = []

# stack overflow for this function
def factors(n):
    return set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

facts = factors(600851475143)


def isprime(n):
    if n == 2:
        ans_list.append(n)
    if n % 2 == 0:
        return
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return
        i += 2
    ans_list.append(n)

for i in facts:
    isprime(i)

print(max(ans_list))
