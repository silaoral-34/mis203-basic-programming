
import random
import time

suspects = ["Alice", "John", "Emma"]
thief = random.choice(suspects)

print("=== THE MISSING DIAMOND ===")
print("A diamond was stolen!")
time.sleep(1)

print("\nSuspects:", suspects)
print("Clue 1: The thief's name starts with", thief[0])
time.sleep(1)
print("Clue 2: You have two chances to solve the case!")

for attempt in range(2):
    answer = input("\nWho is the thief? ").strip().capitalize()

    if answer == thief:
        print("Correct! Mystery solved!")
        break
    else:
        print("Wrong answer! Try again.")
else:
    print("Case closed! The thief was", thief)

print("Thanks for playing!")


