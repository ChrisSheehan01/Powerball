from __future__ import print_function
from collections import Counter
import sys

nameAndFavNums = []

def getNameAndNumbersFromUser():
    getEmployeeNameFromUser()
    getNumbersFromUser()

def getEmployeeNameFromUser():
    print('Enter your first name: ', end='')
    name = sys.stdin.readline()
    print('Enter your last name: ', end='')
    name = name + " " + sys.stdin.readline()
    nameAndFavNums.append(name.replace("\n", ""))


def getNumbersFromUser():
    pos = ['1st', '2nd', '3rd', '4th', '5th', 'Power Ball']
    exclusion = '69'
    userInputComplete = False
    i = 0

    while userInputComplete is False:
        print('Select ' + pos[i] + ' # (1 thru ' + exclusion  + '): ', end='')
        try:
            line = int(raw_input())
            if checkIfValidNum(line) is True:
                nameAndFavNums.append(line)
                i += 1
                if i == 5:
                    exclusion = '26'
                else:
                    if i >= 2:
                        exclusion = '69 excluding ' + str(nameAndFavNums[1:-1]).strip("[").strip("]") + ', and ' + str(nameAndFavNums[-1])
                    else:
                        exclusion = '69 excluding ' + str(nameAndFavNums[1])
                if i == 6:
                    userInputComplete = True
            else:
                print("Invalid integer, try again.")
        except ValueError:
            print("Not an integer, try again.")


def checkIfValidNum(num):
    if len(nameAndFavNums) == 0:
        return True
    if (num >= 1) and (num <= 69):
        if len(nameAndFavNums) == 6:
            if num <= 26:
                return True
            else:
                return False
        elif nameAndFavNums[1:].__contains__(num):
            return False
        else:
            return True
    else:
        return False

def writeToFile(line):
    employeePowerball = open("employeePowerball.txt", "a")
    employeePowerball.write(bytes(line))
    employeePowerball.write("\n")
    employeePowerball.close()

def findNumFrequency():
    employeePowerball = open("employeePowerball.txt", "r")
    text_in_file = employeePowerball.read()
    print ("hi" + str(Counter(text_in_file).most_common(5)))

def printFromFile():
    employeePowerball = open("employeePowerball.txt", "r")
    text_in_file = employeePowerball.read()
    print(text_in_file)

getNameAndNumbersFromUser()
# writeToFile(nameAndFavNums)
# findNumFrequency()
# printFromFile()