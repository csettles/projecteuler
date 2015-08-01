# find greatest product of four adjacent numbers in the same direction
from operator import mul
from functools import reduce

# this will open the text file and convert it to a string
with open("problem11.txt", "r") as f:
    data = f.read().replace('\n', ' ')

rows = data.split()


# this is from stack overflow

# makes everything ints
rows = list(map(int, rows))
# makes into sublists of length 20
rows = [rows[x:x+20] for x in range(0, len(rows), 20)]

# ***runs in 0.2s***
# whew! We are now done making the matrix!
# let's start on these functions...

ans_list = []


# returns the product of all items in a list
def prod(list):
    return reduce(mul, list, 1)


# runs in 0.3s
def get_down(y):
    local_ls = []
    x = 0

    while x < 17:
        var = [rows[x][y], rows[x+1][y], rows[x+2][y], rows[x+3][y]]
        local_ls.append(prod(var))
        x += 1

    return max(local_ls)


# runs in 0.2s
def get_across(x):
    local_ls = []
    y = 0

    while y < 17:
        var = [rows[x][y], rows[x][y+1], rows[x][y+2], rows[x][y+3]]
        # print(prod(var)) # debugging purposes
        local_ls.append(prod(var))
        y += 1

    return max(local_ls)


# runs in 0.3s
def get_diag(x, y):
    local_ls = []

    while x < 17 and y < 17:
        var = [rows[x][y], rows[x+1][y+1], rows[x+2][y+2], rows[x+3][y+3]]
        # print(var, "equals", prod(var)) # debugging purposes
        local_ls.append(prod(var))
        x += 1
        y += 1
    # print(local_ls)
    return max(local_ls)

for i in range(0, 20):
    ans_list.append(get_across(i))

# for i in range(0, 20):
#     ans_list.append(get_down(i))

# for i in range(0, 17):
#     ans_list.append(get_diag(0, i))
#     ans_list.append(get_diag(i, 0))

print(ans_list)
