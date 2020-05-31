# write your function here
def readable_timedelta(delta_days):
    weeks = delta_days//7
    days = delta_days%7
    return "{} week(s) and {} day(s)".format(weeks, days)

# test your function
print(readable_timedelta(10))