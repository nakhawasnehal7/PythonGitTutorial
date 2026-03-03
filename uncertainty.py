# Auther SnehalNakhawa
# Date 10th February 2026
# Description - A guessing game based on the uncertainty principle

guesses = 3
particle_x = 4
particle_y = 6

while guesses > 0:
    print(f"The particle is somewhere in this space!, you have {guesses} change to guess it.")
    guess_x = int(input("What do you think its x coordinates us (1-10)?"))
    guess_y = int(input("What do you think its y coordinates us (1-10)?"))

    if guess_x == particle_x and guess_y == particle_y:
        print(f"Good guess!{particle_x}, {particle_y} was the position!")
        break
    elif guess_x < 1 or guess_x > 10 or guess_y < 1 or guess_y > 10:
        print(f"No guess!{guess_x}, {guess_y} is outside the range!")
    else:
        if guess_x > particle_x:
            print("Bad Luck! The particle x position is less than your x position")
        elif guess_x < particle_x:
            print("Bad Luck! The particle x position is greater than your x position")

        if guess_y > particle_y:
            print("Bad Luck! The particle y position is less than your y position")
        elif guess_y < particle_y:
            print("Bad Luck! The particle y position is greater than your y position")
    guesses -= 1

    if guesses == 0:
        print(f"No! you rann out of chances.({particle_x},{particle_y}) was the particle's position!")
