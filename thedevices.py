# ***************************************************************************

# This is program to view file, add, delete and update the file as per user requirement.

# *****************************************************************************

# To submit on 15 of july for the verification and validation

# importing libraries

import os


# This function is to view the file from txt file.


def view():
    f = list(open('Devices.txt', 'r'))
    i = int(input("Select the option from the list (1,2,3,4 0r 5): "))
    if i == 1:
        print(f[0])
    elif i == 2:
        print(f[1])
    elif i == 3:
        print(f[2])
    elif i == 4:
        print(f[3])
    elif i == 5:
        print(f[4])
    else:
        print("Enter the valid number from set")
        i = input("Select the option from the list (1,2,3,4 0r 5)")


# Ritika
# This function is to add the name into existing txt file
def addition():
    with open('Devices.txt', 'r+') as file:
        with open('temp.txt', 'w') as output:
            # iterate all ines from file
            name = input("Enter new device name and code : ")
            for line in file:
                # if the insert device name contains in a file  then don't write it
                if name not in line.strip('\n'):
                    output.write(line)
                else:
                    print("The device is already exist!!!")
            output.write(f'{name}\n')

    os.replace('temp.txt', 'Devices.txt')
    print("Device has been added successfully!!!")


# Hemanta and Rosy
# This function is to delete the name from existing txt file
def delete():
    with open("Devices.txt", 'r') as file:
        with open('temp.txt', 'w') as output:
            # iterate all ines from file
            code = input("Enter the device code: ")
            for line in file:
                # if the insert code contains in a line then don't write it
                if code not in line.strip('\n'):
                    output.write(line)

    os.replace('temp.txt', 'Devices.txt')
    print("The Device has been remove from the file.")


# padam and bikesh
# This function is to update the file to existing txt file
def update():
    with open("Devices.txt", 'r') as file:
        with open('temp.txt', 'w') as output:
            # iterate all ines from file
            code = input("Enter the device code: ")
            newname = input("Enter the new name for the respective device code: ")
            for line in file:
                # if the insert code contains in a line then don't write it
                if code in line.strip('\n'):
                    output.write(f'{newname} {code}')
                elif code not in line.strip('\n'):
                    output.write(line)

    os.replace('temp.txt', 'Devices.txt')
    print("The device name has been updated!!")


# this function is to exit the program.
def exit():
    print("x")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # view()
    # addition()

    delete()

    # update()
    exit()
