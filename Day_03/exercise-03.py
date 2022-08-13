# Day-03 Exercise

from turtle import width


age = 25
height = 168.5
complexnumber = 1+3j

base = (input('Enter the base: '))
height = (input('Enter the height: '))
areaOfTriangle = 0.5 * (int(base)*int(height))


print(areaOfTriangle)


# perimeter of the triangle
A = (input('Enter side a : '))
B = (input('Enter side b : '))
C = (input('Enter side c : '))

perimeteroftriangle = int(A) + int(B) + int(C)

print(perimeteroftriangle)

# area of rectangle

length = (input('Enter length of the rectangle: '))
width = (input('Enter width of the rectangle: '))

areaOfRectangle = int(length) * int(width)
print(areaOfRectangle)


# area of the circle

pi = 3.14
radius = (input('Enter radius : '))
area_of_circle = int(radius) ** 2 * pi
perimeter_of_circle = 2 * pi * int(radius)

print(perimeter_of_circle)
print(area_of_circle)


# slope
x = (input('Enter slope : '))
y = 2*int(x)-2

print(y)
