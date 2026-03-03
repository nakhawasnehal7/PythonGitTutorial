#Auther SnehalNakhawa
#Date 10th February 2026
#Description - Simulate a baseball hit using a random distance
import random
distance = random.randint(0, 450)

if distance > 400:
    print(f"The ball flew {distance} feet and the batter scored a home run. That the run for the team!")
elif 135 <= distance <= 400:
    print(f"The ball flew {distance} feet and the batter made it to third base!")
elif 10 <= distance <= 134 :
    print(f"The ball flew {distance} feet and the batter made it to second base!")
elif 1 <= distance <=9 :
    print(f"The ball flew {distance} feet because the batter bunted, abd made it to first base!")
else :
    print("The batter has made strike!oh no!")