data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = () # replace with your code
r1, r2, r3 = zip(*data)
data_transpose = (r1, r2, r3)

print(r1, r2, r3)
print(data_transpose)