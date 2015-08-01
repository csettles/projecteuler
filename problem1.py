# find the sum of all the multiples of 3 or 5 below 1000

num_list = [x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]
print(sum(num_list))
