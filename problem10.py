# find the sum of all primes below two million

# start with 2 because 2 is the only even prime
ans = 0


def isprime(n):
    if n == 2:
        return n
    if n % 2 == 0:
        return 0
    limit = int(n**0.5+1)
    for i in range(3, limit, 2):
        if n % i == 0:
            return 0
    return n

# increment by two to conserve processing power
for i in range(3, 2000000, 2):
    ans += isprime(i)

print(ans)
