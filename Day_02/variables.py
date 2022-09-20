# Day 2: 30 Days of python programming

# Exercises: Level 1

from __future__ import division
from math import remainder


first_name = 'manoj'
last_name = 'k'
full_name = first_name + ' ' + last_name
country = 'India'
city = 'Hyderabad'
age = 25
year = 2022
is_married = False
is_true = True
is_light_on = True

# Declaring multiple variable on one line
brand, model, mf_year, price, popularity = 'Hyundai', 'creta', 22, 1800000, 'high'

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

first_name_length = (len(first_name))
last_name_length = (len(last_name))

print(first_name_length == last_name_length)

#challenge- Day2-4
num_one, num_two = 5, 4
total = num_one+num_two
diff = num_two-num_one
product = num_one*num_two
division = num_one/num_two
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one//num_two

#challenge- Day2-5

radius = input('enter the radius')
radius = int(radius)
area_of_circle = 3.142 * (radius ** 2)
cir_of_circle = 2*3.142*radius
print(area_of_circle)
print(cir_of_circle)

#challenge- Day2-6
first_name = input("first_name  ")
last_name = input('last_name  ')
country = input('country  ')
age = input('age  ')
age = int(age)

print(type(age))
