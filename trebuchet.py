# Auther SnehalNakhawa
# Date 24th February 2026
# Description - This program records trebuchet trial distance
# and keep of the top three farthest distance along

top_distance = [0, 0, 0]
top_trails = [0, 0, 0]

continue_input = "Y"
trial_number = 1

while continue_input == "Y":
    distance = int(input(f"Please enter your distance for trail{trial_number}:"))

    if distance > top_distance[0]:
        top_distance[2] = top_distance[1]
        top_trails[2] = top_trails[1]

        top_distance[1] = top_distance[0]
        top_trails[1] = top_trails[0]

        top_distance[0] = distance
        top_trails[0] = trial_number

    elif distance > top_distance[1]:
        top_distance[2] = top_distance[1]
        top_trails[2] = top_trails[1]

        top_distance[1] = distance
        top_trails[1] = trial_number
    elif distance > top_distance[2]:
        top_distance[2] = distance
        top_trails[2] = trial_number

    continue_input = input("Would you like to input another trial ? (Y/N):")
    trial_number += 1

print("\n The top three distance for the trebuchet are:")
print(f"{'Trial':<8}{'Distance':<8}")

for i in range(3):
    print(f"{top_trails[i]:<8}{top_distance[i]:<8}")
