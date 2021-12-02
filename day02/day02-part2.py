#! /usr/bin/python3

# read input
with open("input.txt") as file:
    course = []
    for line in file:
        course.append(line.rstrip())
        
# calculated position
horizontal = 0
vertical = 0
aim = 0
product = 0

for i in course:
    i = i.split()
    # print(i[1]," is type ",type(i[1]))
    if i[0] == "forward":
        horizontal += int(i[1])
        vertical += int(i[1])*aim
    elif i[0] == "up":
        aim -= int(i[1])
    elif i[0] == "down":
        aim += int(i[1])
    else:
        print("something went wrong")

# multiply horizontal and vertical position
product = horizontal * vertical

# print results
print("vertical position is ",vertical)
print("horizontal position is ",horizontal)
print("product is ",product)




