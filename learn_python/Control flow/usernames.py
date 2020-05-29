names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    converted_name = name.lower()
    converted_name = converted_name.replace(' ','_')
    usernames.append(converted_name)

print(usernames)