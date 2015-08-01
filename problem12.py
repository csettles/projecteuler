# find the first triangle number that has over 500 factors


# for some reason, creating a list like this and using sum()
# is faster than using (n(n+1))/2

ls = range(1, 100000)


def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result


for i in range(10000, 100000):
    triangle_num = sum(ls[:i])
    if len(factors(triangle_num)) > 500:
        print(triangle_num)
        break
