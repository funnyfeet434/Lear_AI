names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [first_name.lower()[0:(first_name.find(' '))] for first_name in names]# write your list comprehension here
print(first_names)