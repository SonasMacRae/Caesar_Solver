import enchant
import os


def Encrypt(message, key):
    os.system('cls||clear')
    output = ""

    for x in message.lower():
        if x == ' ':
            output += ' '
            continue

        if ord(x) < 97 or ord(x) > 122:
            continue

        else:
            newLetter = ord(x) + key
            if newLetter > 122:
                newLetter -= 26
            output += chr(newLetter)

    return output


def Decrypt(message, key):
    os.system('cls||clear')

    output = ""

    for x in message.lower():
        if x == ' ':
            output += ' '
            continue

        if ord(x) < 97 or ord(x) > 122:
            continue

        else:
            newLetter = ord(x) - key

            if newLetter < 97:
                newLetter += 26
            output += chr(newLetter)

    return output


def AutoSolver(message):
    os.system('cls||clear')

    d = enchant.Dict("en_US")
    e = enchant.Dict("en_UK")

    bestScore = 0
    key = 0
    output = ""
    for x in range(26):
        counter = 0
        temp = Decrypt(message,x)
        tempList = temp.split(' ')
        for y in tempList:
            if d.check(y) == True or e.check(y) == True:
                counter += 1
        if counter > bestScore:
            bestScore = counter
            output = temp
            key = x

    newOutput = "Input: " + message + "\nOutput: " + output + "\nThe key was: " + str(key)
    return newOutput


def App():
    temp = ""

    while temp != "Q" or temp != "q":
        choice = False

        os.system('cls||clear')
        print("Caesar cipher stuff\n")

        print("1 - Encrypt a message")
        print("2 - Decrypt a message")
        print("3 - Decrypt a message without a key")
        print("q - Quit")

        temp = input()
        os.system('cls||clear')

        if temp == "1":
            message = input("Input your message ")
            key = int(input("Input your key "))
            print(Encrypt(message, key))
            choice = True
            print("Press Enter key to continue")
            temp = input()

        if temp == "2":
            message = input("Input your message ")
            key = int(input("Input your key "))
            print(Decrypt(message, key))
            choice = True
            print("Press Enter key to continue")
            temp = input()

        if temp == "3":
            message = input("Input your message ")
            choice = True
            print(AutoSolver(message))
            print("Press Enter key to continue")
            temp = input()

        if temp == "q":
            return

        if choice == False:
            print("Command not recognised, enter a number between 1 and 4\n")





App()
