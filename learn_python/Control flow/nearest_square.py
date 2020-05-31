limit = 40

# write your while loop here
i = 1
nearest_square = 0

while i**2 <= limit:
    nearest_square = i**2
    i += 1



print(nearest_square)