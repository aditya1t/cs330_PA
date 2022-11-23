# cs330_PA

The language of this program is Python. The code above simulates a security system used in everyday use. The system has a keypad with ten keys, labeled from '0' to '9'. The security engine will unlock the lock when it finds the correct un-locking access code in the input string. Likewise, the security engine will lock the lock when it finds the correct locking access code in the input string.

The code allows the user to input their student ID, which is then used to generate the unlocking and locking codes. The code will then accept a string of numbers from the user and will check to see if the unlocking or locking code is contained within it. If so, then appropriate action will be taken (lock or unlock).

In part 2, the code estimates how long it would take to break the lock if an intruder did not know the length of the access string. This is done by simulating the input of a random string of numbers and checking to see if the lock is unlocked after each digit is input. The code then repeats this process 10 times and reports the minimum, maximum, and average number of digits that were input before the lock was unlocked.

Overall, the code provides a way to simulate a security system and to estimate the time it would take to break the lock if the intruder did not know the length of the access code.

There are a few things that could be improved with the code. First, the code only works for a student ID that is 5 digits long. This could be changed so that it would work for any length of student ID. Second, the code only works for an access code that is 5 digits long. Again, this could be changed to work for any length of access code. Finally, the code only estimates the time it would take to break the lock if the intruder did not know the length of the access code. It would be interesting to also estimate the time it would take if the intruder knew the length of the access code
