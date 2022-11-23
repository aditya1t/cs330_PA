import random
 
def main():

    numSymbols = 10 # average number of digits to access string
    numTries = 10000 # total number of times to try
    total = 0 # total number of tries done 
    for i in range(numTries):
        symbols = generateSymbols(numSymbols) # generates random sequence
        tries = checkLock(symbols) # check if lock is unlocked
        total += tries
        print("Average number of tries:", total / numTries)
 
def generateSymbols(numSymbols):
# Generate a random sequence of numerical digits
    symbols = []
    for i in range(numSymbols):
        symbols.append(random.randint(0, 9))
        return symbols
 
def checkLock(symbols):
# Check if the lock is unlocked
    tries = 1
    while not isUnlocked(symbols):
        tries += 1
        return tries

def isUnlocked(symbols):
# Check if the lock is unlocked
    unlocked = True
    for i in range(len(symbols) - 1):
        if symbols[i] != symbols[i + 1]:
            unlocked = False
            return unlocked
main()