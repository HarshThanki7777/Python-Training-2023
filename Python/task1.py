# # 1) Convert Months into no. of years
    
#       months = 24
#       years = ??

# 2) Convert Years into months
    
#      years = 4
#      months = ?

# 3) convert days into months and years

#          days = 750
#          months = ?
#          years = ?

# from calendar import month


months = 24
years = months // 12
print(years)


years = 4
months = years * 12
print(months)

days = 750
years = days // 365
remaining_days = days % 365
months = remaining_days // 30
print(years, months)





