#Author SnehalNakhawa
#Date 24th February 2026
#Description - This program simulates an 8X8 cosmic ray muon detector map
#Find the highest and lowest capture rates, and print the grid


import  random

MAP_SIZE = 8

moun_map = []
for i in range(MAP_SIZE):
    row = []
    for j in range(MAP_SIZE):
        row.append(0)
    moun_map.append(row)


for i in range(MAP_SIZE):
    for j in range(MAP_SIZE):
        moun_map[i][j] = random.randint(0, 500)


highest_value = -1
lowest_value = 501

highest_x = highest_y= 0
lowest_x = lowest_y = 0


for i in range(MAP_SIZE):
    for j in range(MAP_SIZE):
        value = moun_map[i][j]

        if value > highest_value:
            highest_value = value
            highest_x =i
            highest_y = j


        if value <lowest_value:
            lowest_value = value
            lowest_x = i
            lowest_y = j





print(f"The highest capture rate  was {highest_value} at location {highest_x+1}, {highest_y+1}.")
print(f"The lowest capture rate  was {lowest_value} at location {lowest_x+1}, {lowest_y+1}.\n")

print("The map looks like the following:")

for row in moun_map:
    for val in row:
        print(f"{val:4}", end =  "" )

    print()


















