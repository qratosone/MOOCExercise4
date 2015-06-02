def is_leap_year(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True
    else:
        return False
def get_num_of_days_in_month(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28
def get_total_num_of_days(year,month):
    total=0
    for y in range(1800,year):
        if is_leap_year(y):
            total+=366
        else:
            total+=365
    for m in range(1,month):
        total+=get_num_of_days_in_month(year,m)
    return total
def get_start_day(year,month):
    return (2+get_total_num_of_days(year,month)+get_num_of_days_in_month(year,month))%7
year=input()
month=input()
print get_start_day(year,month)

