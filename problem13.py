# find the first 10 digits of the 100 50-digit ints

with open('problem13.txt', 'r') as f:
    data = f.read().replace('\n', ' ')

ls = data.split()

# makes everything ints
nums = list(map(int, ls))


first_10 = str(sum(nums))
print(first_10[:10])
