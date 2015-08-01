# find a palindrome with two three digit factors

rng = list(range(10000, 998001))
possible = []
ans_set = []


def palindrome_checker(n):
    str_n = str(n)
    length = len(str_n)//2
    first = str_n[:length]
    last = str_n[length:]
    if first == last[::-1]:
        possible.append(n)
    else:
        return

for i in rng:
    palindrome_checker(i)


# factors is from stack overflow, but everything else is from me
def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

for x in possible:
    facts = factors(x)
    tally = 0
    for y in facts:
        if (99 < y < 1000) and (99 < (x / y) < 1000):
            tally += 1
        else:
            continue
    if tally > 0:
        ans_set.append(x)

print(max(ans_set))
