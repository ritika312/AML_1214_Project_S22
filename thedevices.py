# ***************************************************************************

# This is program to view file, add, delete and update the file as per user requirement.

# *****************************************************************************

# To submit on 15 of july for the verification and validation

# importing libraries

import os
import linecache

func_list = ['add', 'view', 'delete', 'update']


# This function is to ask what user want to perform for this application.
def user_function():
    print("What would you like to do?(Add, view, delete, update)")
    answer = input("Select the function you like to do: ")
    if any(answer.lower() == f for f in func_list):
        return answer
    else:
        print("Enter the valid function name!!")


def check(fname):
    try:
        if fname == 'add':
            addition()
        elif fname == 'view':
            view()
        elif fname == 'delete':
            delete()
        elif fname == 'update':
            update()
    except Exception as e:
        print("Function name doesn't exit check the valid function name" + str(e))
    print('-------------------------------------------------------------')
    answer = input("Do you want to continue ? Y/N:  ")
    try:
        if any(answer.lower() == f for f in ["yes", "y"]):
            result = user_function()
            check(result)
        elif any(answer.lower() == f for f in ["no", "n"]):
            exit_program()
            exit()
        else:
            print('Please enter yes or no')
    except Exception as e:
        print("Error has occurred :" + str(e))


# This function is to view the file from txt file.
def view():
    print('-------------------------------------------------------------')
    print("What would you  like to view(all or specific device no)")
    ans = input(" Do you want to view all ?(Y/N) ")
    if any(ans.lower() == f for f in ["yes", "y"]):
        try:
            with open('Devices.txt', 'r') as file:
                print("This is all the device list")
                print(file.read())
        except FileExistsError as f:
            print("File does not exit : " + str(f))
    elif any(ans.lower() == f for f in ["no", 'n']):
        try:
            line_no = int(input("Select the line number form the list(1,2,3,4,5..."))
            line = linecache.getline(r"Devices.txt", line_no)
            print(f"This is the device listed in line no : {line_no}", f"\n{line}")
        except Exception as e:
            print("Line number does not exist :" + str(e))
    else:
        print("Invalid response")


# Ritika
# This function is to add the name into existing txt file
def addition():
    try:
        with open('Devices.txt', 'r+') as file:
            with open('temp.txt', 'w') as output:
                try:
                    print('-------------------------------------------------------------')
                    device_name = input("Enter new device name : ")
                    device_code = input("Enter new device code: ")
                    # check if the input name is alphbet and code is alphanumeric
                    if device_name.isalpha() and device_code.isalnum():
                        try:
                            # iterate all lines from file
                            for line in file:
                                # if the insert device name contains in a file  then don't write it
                                if device_name and device_code in line.strip('\n'):
                                    output.write(line)
                                else:
                                    output.write(line)
                            output.write(f'{device_name} {device_code}\n')

                        except Exception as e:
                            print("Error has occurred in for loop statement" + str(e))
                    else:
                        print("Invalid input. Please enter the name or code :")
                        addition()
                except ValueError as e:
                    print("Error has occurred" + str(e))

        os.replace('temp.txt', 'Devices.txt')
    except FileExistsError as e:
        print("Error has occurred while opening file" + str(e))
    print(f"Device : {device_name} {device_code} has been added successfully!!!")


# Hemanta and Rosy
# This function is to delete the name from existing txt file
def delete():
    try:
        with open("Devices.txt", 'r') as file:
            with open('temp.txt', 'w') as output:
                # iterate all lines from file
                try:
                    print('-------------------------------------------------------------')
                    code = input("Enter the device code: ")
                    if code.isalnum():
                        try:
                            for line in file:
                                # if the insert code contains in a line then don't write it
                                if code not in line.strip('\n'):
                                    output.write(line)
                        except Exception as e:
                            print("Error has occurred in for loop statement" + str(e))
                    else:
                        print("Invalid input. Please enter code again!!")

                except ValueError as e:
                    print("Error has occurred" + str(e))
        os.replace('temp.txt', 'Devices.txt')
    except FileExistsError as e:
        print("Error has occurred while opening file" + str(e))
    print(f"Device with code : {code} has been remove from the file.")


# padam and bikesh
# This function is to update the file to existing txt file
def update():
    try:
        with open("Devices.txt", 'r') as file:
            with open('temp.txt', 'w') as output:
                try:
                    print('-------------------------------------------------------------')
                    code = input("Enter the device code: ")
                    if code.isalnum():
                        try:
                            for line in file:
                                # if the insert code contains in a line then don't write it
                                if code in line.strip('\n'):
                                    newname = input("\nEnter the new name for the respective device code: ")
                                    output.write(f'{newname} {code}')
                                elif code not in line.strip('\n'):
                                    output.write(line)

                        except Exception as e:
                            print("Error has occurred in for loop statement" + str(e))
                    else:
                        print("Invalid input. Please enter the valid code and new name!!!")


                except ValueError as e:
                    print("Error has occurred" + str(e))

        os.replace('temp.txt', 'Devices.txt')
    except FileExistsError as e:
        print("Error has occurred while opening file" + str(e))
    print(f"Device name : {newname}{code} has been updated!!")


# this function is to exit the program.
def exit_program():
    print("Thanks for using the application !")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("**************************************************")
    print("---Welcome to Computer Device Management System---")
    print("**************************************************")
    response = user_function()
    check(response)
