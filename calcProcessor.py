import sys
import math

def processFile():   
    filename = input("Please enter the file containig the operations to perform: ")
    
    ops = open(filename,"r")
    
    for line in ops:
        line = line.strip()
        pieces = line.split(" ")
        
        if len(pieces) != 3:
            raise Exception(f"Looks like some data is missing on line: {line}")
        
        if pieces[1] == "+":
            x = int(pieces[0])
            y = int(pieces[2])
            z = x + y
            print(f"{x} + {y} = {z}")
        elif pieces[1] == "-":
            x = int(pieces[0])
            y = int(pieces[2])
            z = x - y
            print(f"{x} + {y} = {z}")
        elif pieces[1] == "*":
            x = int(pieces[0])
            y = int(pieces[2])
            z = x * y
            print(f"{x} * {y} = {z}")
        elif pieces[1] == "/":
            x = int(pieces[0])
            y = int(pieces[2])
            z = x / y
            print(f"{x} / {y} = {z}")
        else:
            y = int(pieces[2])
            z = math.sqrt(y)
            print(f"√{y} = {z}")    

def main():
    try:
        processFile()
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Oh no! It seems that file did not exist!")        
    except ValueError as ve:
        print(ve)
        print("Uh oh! Looks like one of the operations had a bad type in it!")
    except ZeroDivisionError as zde:
        print(zde)
        print("Boo! One of the operations has division by 0")
    except:
        print("Wow! Something went wrong that we did not forsee!")
        # sys.exit(-1)
    else:
        print("Looks like everything went smoothly.")
    


main()