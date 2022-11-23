#Tekale Aditya, A20517287

# part 1

stud_id = input("Enter first five digits of your student ID: ")
unlocking_passcode = stud_id[-5:] + "1"
locking_passcode = stud_id[-5:] + "4"

user_input = input("Enter a string of numbers: ")

if unlocking_passcode in user_input:
    print("Unlocked")
elif locking_passcode in user_input:
    print("Locked")
else:
    print("Invalid code")

print('Code has run successfully')

# part 2

import random

def breaking_lock():
    num_symbols = 0
    while True:
        num_symbols += 1
        user_input = str(random.randint(0,9))
        if unlocking_passcode in user_input:
            return num_symbols

results = []
for i in range(10):
    results.append(breaking_lock())

    print("Minimum:", min(results))
    print("Maximum:", max(results))
    print("Average:", sum(results)/len(results))