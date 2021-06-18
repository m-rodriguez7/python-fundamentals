'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
import math

radius = 3.14
height = 5
pi = math.pi

surface_area = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
volume = pi * (radius ** 2) * height

print(f'Volume: {volume}')
print(f'Surface area: {surface_area}')