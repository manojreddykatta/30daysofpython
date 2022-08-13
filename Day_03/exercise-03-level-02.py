# task 3.8
x = input('enter x : ')
y = 2*int(x)-2
print(y)

# task 3.9

x1 = input('enter x1 : ')
x2 = input('enter x2 : ')
y1 = input('enter y1 : ')
y2 = input('enter y2 : ')

m = int(y2)-int(y1)/int(x2)-int(x1)
print(m)

# task 3.10

print(y == m)

# task 3.11
a = int(input('enter a : '))
b = a**2+6*a+9

print(b)

# task 3.12
str_one = 'pyhton'
str_two = 'dragon'

print(not len(str_one) == len(str_two))

# task 3.13
is_on_in_python = 'on' in str_one
is_on_in_dragon = 'on' in str_two

print(is_on_in_python and is_on_in_dragon)

# task 3.14
sentence = 'I hope this course is not full of jargon'
print('in operator check ', 'jargon' in sentence)

# task 3.15
print(not is_on_in_python and is_on_in_dragon)

# task 3.16
length_of_str_one = len(str_one)
print(float(length_of_str_one))
print(str(length_of_str_one))

# task 3.17
number = input('Enter a number : ')
is_even = int(number)/2

print(is_even)

# task 3.18
m, n = 7, 3
fd = m//n
o = 2.7
int_o = int(o)
print(fd == int_o)

# task 3.19
d = '10'
e = 10
is_type_check = (type(d) == type(e))
print(is_type_check)

# task 3.20
print(int('9.8') == 10)

# task 3.21
hours = input('Enter hours : ')
rate_per_hour = input('Rate per hour :')
weekly_earnings = int(rate_per_hour) * int(hours)
print(weekly_earnings)

# task 3.22
years = input('Enter years : ')
seconds_lived = 31536000 * int(years)
