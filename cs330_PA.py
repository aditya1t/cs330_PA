student_id = input("Enter your student ID: ")
unlocking_code = student_id[-5:] + "1"
locking_code = student_id[-5:] + "4"

user_input = input("Enter a string of numbers: ")

if unlocking_code in user_input:
    print("Unlocked")
elif locking_code in user_input:
    print("Locked")
else:
    print("Invalid code")

import random

def breaking_lock():
    num_symbols = 0
    while True:
        num_symbols += 1
        user_input = str(random.randint(0,9))
        if unlocking_code in user_input:
            return num_symbols

results = []
for i in range(10):
    results.append(breaking_lock())

print("Minimum:", min(results))
print("Maximum:", max(results))
print("Average:", sum(results)/len(results))