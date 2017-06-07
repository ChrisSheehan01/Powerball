from __future__ import print_function
from collections import Counter
from random import randint


nameAndFavNums = []
allNamesAndNums = []
columnCounts = []
finalTicket = []


def user_input():
    employee_name_input()
    get_fav_num_input()


def employee_name_input():
    print('Enter your first name: ', end='')
    name = raw_input()
    print('Enter your last name: ', end='')
    name = name + " " + raw_input()
    nameAndFavNums.append(name)


def get_fav_num_input():
    pos = ['1st', '2nd', '3rd', '4th', '5th', 'Power Ball']
    exclusion = '69'
    input_complete = False
    i = 0

    while input_complete is False:
        print('Select ' + pos[i] + ' # (1 thru ' + exclusion + '): ', end='')
        try:
            line = int(raw_input())
            if valid_num_input(line) is True:
                nameAndFavNums.append(line)
                i += 1
                if i == 5:
                    exclusion = '26'
                else:
                    if i >= 2:
                        exclusion = '69 excluding ' + str(nameAndFavNums[1:-1]).translate(None, "[]") \
                                    + ', and ' + str(nameAndFavNums[-1])
                    else:
                        exclusion = '69 excluding ' + str(nameAndFavNums[1])
                if i == 6:
                    input_complete = True
            else:
                print("Invalid integer, try again. ", end='')
        except ValueError:
            print("Not an integer, try again. ", end='')
    print()


def valid_num_input(num):
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


def write_picks_to_file(line):
    powerball_data = open("employeePowerball.txt", "a")
    powerball_data.write(bytes(str(line).strip("[").strip("]")))
    powerball_data.write("\n")
    powerball_data.close()


def combine_all_data():
    with open('employeePowerball.txt', 'r') as input_file:
        for line in input_file:
            text_line = list(line.strip("\n").split(", "))
            allNamesAndNums.append(text_line)
    input_file.close()


def find_num_freq():
    for i in range(1, 7):
        columns = []
        for eachList in allNamesAndNums:
            columns.append(eachList[i])
        columnCounts.append(Counter(columns))


def calculate_final_powerball():
    for counter in columnCounts:
        max_val = counter.most_common(1)[0][1]
        most_freq_nums = []
        j = 0
        for i in counter:
            if counter[i] == max_val:
                most_freq_nums.append(counter.keys()[j])
            j += 1
        finalTicket.append(most_freq_nums[randint(0, len(most_freq_nums) - 1)])


def print_all_employee_picks():
    with open('employeePowerball.txt', 'r') as input_file:
        for line in input_file:
            text_line = list(line.strip("\n").split(", "))
            print(text_line[0].strip("'"), end=" ")
            for i in text_line[1:-1]:
                print(i + " ", end="")
            print("Powerball: " + str(text_line[-1]))
    input_file.close()


def delete_data():
    open('employeePowerball.txt', 'w').close()
    print("\nAll data removed!")


def main():
    user_input()
    write_picks_to_file(nameAndFavNums)
    combine_all_data()
    find_num_freq()
    calculate_final_powerball()
    print_all_employee_picks()
    print("\nPowerball winning number: \n" + str(finalTicket[:-1]).translate(None, "',[]")
          + " Powerball: " + str(finalTicket[-1]))

    repeat = True
    while repeat is True:
        print('\nDelete all data on record?(y/n): ', end='')
        data_remove = raw_input()

        if data_remove == 'y':
            delete_data()
        if data_remove == 'n' or data_remove == 'y':
            print("\nGoodbye!")
            repeat = False

if __name__ == '__main__':
    main()
