import os

filename = input("Please enter the name of the file: ")

# if os.path.exists(filename):
#     print(f"{filename} exists!")
# else:
#     print(f"{filename} does not exist!")
    
# myFile = open(filename,"w")

myFile = open(filename,"x")

number = int(input("What number do you want me to start logging values from: "))

for x in range(number,number+10):
    myFile.write(f"{x}\n")

myFile.close()
