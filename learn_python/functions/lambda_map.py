numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

#def mean(num_list):
#    return sum(num_list) / len(num_list)


averages = list(map(lambda x: sum(x) / len(x), numbers)) #list(map(mean, numbers))
print(averages)