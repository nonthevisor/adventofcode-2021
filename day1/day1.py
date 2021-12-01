#! /usr/bin/python3

# get input
with open("input.txt") as file:
    measurements=[]
    for line in file:
        measurements.append(int(line.rstrip()))

# check if i is greater than i-1
count = 0
for i in range(len(measurements)):
    if measurements[i] > measurements[i-1]:
        print(measurements[i], " is greater than ", measurements[i-1])
        count += 1
print(count)
