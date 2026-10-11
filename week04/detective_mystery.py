import random
import time

suspects = ["Alice", "John", "Emma"]
thief = random.choice(suspects)

print("=== THE MISSING DIAMOND ===")
print("A diamond was stolen last night!")
time.sleep(1)

print("\nSuspects:", suspects)
print("\nClue 1: The thief was wearing a black jacket.")
time.sleep(1)
print("Clue 2: The thief was seen near the library.")
time.sleep(1)

clues = {
    "Alice": "She was in the kitchen.",
    "John": "He was near the library.",
    "Emma": "She was in the garden."
}

print("\nWitness reports:")
for name, clue in clues.items():
    print(name + ":", clue)

answer = input("\nWho is the thief? ").strip().capitalize()

if answer == thief:
    print("Correct! You solved the mystery!")
else:
    print("Wrong suspect! The thief was", thief)

print("\nCase closed.")





