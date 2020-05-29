mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
total_sales = int(mon_sales)
total_sales += int(tues_sales)
total_sales += int(wed_sales)
total_sales += int(thurs_sales)
total_sales += int(fri_sales)

print("This week's total sales: " + str(total_sales))