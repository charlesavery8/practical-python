# bounce.py
#
# Exercise 1.5
height = 100
bounces = 0
while height > 1:
    height = height * .6
    bounces +=1
    print(bounces, (height))