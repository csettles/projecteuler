# smallest positive integer evenly divisible by nums in range(1, 21)
# num must be <= 20! which is 2432902008176640000
# finished in 6.9 seconds

ans = []

check = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

prime = 92378  # product of primes in check times 2 to account for even factors
product_check = 670442572800  # equal to 20!/10!

for i in range(0, product_check, prime):
    if all(i % n == 0 for n in check):
        ans.append(i)
    else:
        continue

ans.remove(0)
print(min(ans))
