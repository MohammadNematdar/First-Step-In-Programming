from math import floor,ceil
age = int(input('please enter your age in days: '))
years = (floor(age/365))
age = (age/365 - floor(age/365))*365
months = floor(age/30)
age = (age/30 - floor(age/30))*30
weeks = floor(age/7)
age = (age/7 - floor(age/7))*7
days = ceil(age)
print('your age is {0} years, {1} month, {2} weeks and {3} days'.format(years,months,weeks,days))
