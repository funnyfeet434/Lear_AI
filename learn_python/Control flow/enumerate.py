cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for num, name in enumerate(cast):
    cast[num] += ' ' + str(heights[num])


print(cast)