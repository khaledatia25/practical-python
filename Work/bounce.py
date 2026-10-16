# bounce.py
#
# Exercise 1.5

height = 100.0
bounce = 1

for i in range(10):
    bounce_height = height * .6
    print(bounce, round(bounce_height, ndigits=4))
    height = bounce_height
    bounce += 1
