import os

filename = input("Please enter the name of the file: ")

while os.path.exists(filename):
    filename = input("That file does not exist! Please enter the name of the file: ")


# file = open(filename,"r")
#
# fullText = file.read()
#
# print(fullText)
#
# file.close()
#
# print("\n------------------------------------\n")
#
# file = open(filename,"r")
#
# someText = file.read(8)
#
# print(f"\"{someText}\"")
#
# someMoreText = file.readline()
#
# print(f"\"{someMoreText}\"")
#
# file.close()

print("\n------------------------------------\n")

# file = open(filename,"r")
#
# for line in file:
#     print(line)
#
# # file.close()

print("\n------------------------------------\n")

# file = open(filename,"r")
#
# line = file.readline()
#
# while line:
#     print(line)
#
#     line = file.readline()
#
# # file.close()

print("\n------------------------------------\n")

with open(filename,"r") as file:
    for line in file:
        print(line)
