from __future__ import print_function
import sys

favNums = []

def getUserInput():
    print('Enter your first name: ', end='')
    employeeName = sys.stdin.readline()
    print('Enter your last name: ', end='')
    employeeName = employeeName + " " + sys.stdin.readline()

    favNums.append(employeeName.replace("\n", ""))

    print('select 1st # (1 thru 69): ', end='')
    favNums.append(sys.stdin.readline().replace("\n", ""))
    print('select 2nd # (1 thru 69 excluding' + str(favNums[1:]) + '): ', end='')
    favNums.append(sys.stdin.readline().replace("\n", ""))
    print('select 3rd # (1 thru 69 excluding' + str(favNums[1:]) + '): ', end='')
    favNums.append(sys.stdin.readline().replace("\n", ""))
    print('select 4th # (1 thru 69 excluding' + str(favNums[1:]) + '): ', end='')
    favNums.append(sys.stdin.readline().replace("\n", ""))
    print('select 5th # (1 thru 69 excluding' + str(favNums[1:]) + '): ', end='')
    favNums.append(sys.stdin.readline().replace("\n", ""))
    print('select Power Ball # (1 thru 26): ', end='')
    favNums.append(sys.stdin.readline().replace("\n", ""))

def writeToFile(line):
    employeePowerball = open("employeePowerball.txt", "a")
    employeePowerball.write(bytes(line))
    employeePowerball.close()

def printFromFile():
    employeePowerball = open("employeePowerball.txt", "r")
    text_in_file = employeePowerball.read()
    print(text_in_file)


getUserInput()
writeToFile(favNums)
printFromFile()