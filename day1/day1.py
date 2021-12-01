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

# check if sum of i+1,i+2,i+3 is greater than sum of i,i+1,i+2
slide_count = 0
for i in range(len(measurements)):
    try:
        slide_window_cur = measurements[i]+measurements[i+1]+measurements[i+2]
        slide_window_sub = measurements[i+1]+measurements[i+2]+measurements[i+3]
        if slide_window_sub > slide_window_cur:
            print(slide_window_sub, " is greater than ", slide_window_cur)
            slide_count += 1
    except:
        print("cannot form a subsequent sliding window")
print(slide_count)
