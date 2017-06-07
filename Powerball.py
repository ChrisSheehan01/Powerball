from __future__ import print_function
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
    print('Select 1st # (1 thru 69): ', end='')
    if checkIfValidNum(sys.stdin.readline().replace("\n", "")):
        nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('Select 2nd # (1 thru 69 excluding' + str(nameAndFavNums[1:]) + '): ', end='')
    if checkIfValidNum(sys.stdin.readline().replace("\n", "")):
        nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('Select 3rd # (1 thru 69 excluding' + str(nameAndFavNums[1:]) + '): ', end='')
    if checkIfValidNum(sys.stdin.readline().replace("\n", "")):
        nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('Select 4th # (1 thru 69 excluding' + str(nameAndFavNums[1:]) + '): ', end='')
    if checkIfValidNum(sys.stdin.readline().replace("\n", "")):
        nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('Select 5th # (1 thru 69 excluding' + str(nameAndFavNums[1:]) + '): ', end='')
    if checkIfValidNum(sys.stdin.readline().replace("\n", "")):
        nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('Select Power Ball # (1 thru 26): ', end='')
    if checkIfValidNum(sys.stdin.readline().replace("\n", "")):
        nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))

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
    employeePowerball.close()

def printFromFile():
    employeePowerball = open("employeePowerball.txt", "r")
    text_in_file = employeePowerball.read()
    print(text_in_file)

# getNameAndNumbersFromUser()
# writeToFile(nameAndFavNums)
# printFromFile()