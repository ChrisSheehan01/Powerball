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
    print('select 1st # (1 thru 69): ', end='')
    nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('select 2nd # (1 thru 69 excluding' + str(nameAndFavNums[1:]) + '): ', end='')
    nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('select 3rd # (1 thru 69 excluding' + str(nameAndFavNums[1:]) + '): ', end='')
    nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('select 4th # (1 thru 69 excluding' + str(nameAndFavNums[1:]) + '): ', end='')
    nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('select 5th # (1 thru 69 excluding' + str(nameAndFavNums[1:]) + '): ', end='')
    nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))
    print('select Power Ball # (1 thru 26): ', end='')
    nameAndFavNums.append(sys.stdin.readline().replace("\n", ""))

def writeToFile(line):
    employeePowerball = open("employeePowerball.txt", "a")
    employeePowerball.write(bytes(line))
    employeePowerball.close()

def printFromFile():
    employeePowerball = open("employeePowerball.txt", "r")
    text_in_file = employeePowerball.read()
    print(text_in_file)

getNameAndNumbersFromUser()
writeToFile(nameAndFavNums)
printFromFile()