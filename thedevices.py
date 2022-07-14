# ***************************************************************************

# This is program to view file, add, delete and update the file as per user requirement.

# *****************************************************************************

# To submit on 15 of july for the verification and validation

# importing libraries

import os
import linecache

# This function is to view the file from txt file.


def view():
    line_no = int(input("Select the line number form the list(1,2,3,4,5..."))
    line = linecache.getline(r"Devices.txt", line_no)
    print(line)

# Ritika
# This function is to add the name into existing txt file
def addition():
    try:
        with open('Devices.txt', 'r+') as file:
            with open('temp.txt', 'w') as output:
                try:
                    device_name = input("Enter new device name and code : ")
                    # check if the input name is alphanumeric
                    if device_name.isalnum():
                        try:
                            # iterate all lines from file
                            for line in file:
                                # if the insert device name contains in a file  then don't write it
                                if device_name not in line.strip('\n'):
                                    output.write(line)
                                else:
                                    print("The device is already exist!!!")
                            output.write(f'{device_name}\n')
                        except Exception as e:
                            print("Error has occurred in for loop statement" + str(e))
                    else:
                        print("Invalid input. Please enter the name and code simultaneously")
                except ValueError as e:
                    print("Error has occurred" + str(e))

        os.replace('temp.txt', 'Devices.txt')
    except FileExistsError as e:
        print("Error has occurred while opening file" + str(e))
    print("Device has been added successfully!!!")


# Hemanta and Rosy
# This function is to delete the name from existing txt file
def delete():
    try:
        with open("Devices.txt", 'r') as file:
            with open('temp.txt', 'w') as output:
                # iterate all lines from file
                try:
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
                        code = input("Enter the device code: ")
                except ValueError as e:
                    print("Error has occurred" + str(e))
        os.replace('temp.txt', 'Devices.txt')
    except FileExistsError as e:
        print("Error has occurred while opening file" + str(e))
    print("The Device has been remove from the file.")


# padam and bikesh
# This function is to update the file to existing txt file
def update():
    try:
        with open("Devices.txt", 'r') as file:
            with open('temp.txt', 'w') as output:
                try:
                    code = input("Enter the device code: ")
                    newname = input("Enter the new name for the respective device code: ")
                    if code.isalnum() and newname.isalpha():
                        try:
                            for line in file:
                                # if the insert code contains in a line then don't write it
                                if code in line.strip('\n'):
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
    print("The device name has been updated!!")


# this function is to exit the program.
def exit():
    print("x")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    view()
    # addition()

    # delete()

    # update()
    exit()
