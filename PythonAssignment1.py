import math
# Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.


def program1():
    output = []
    for i in range(2000, 3200):
        if i % 7 == 0 and i % 5 != 0:
            output.append(i)
    print(','.join(str(no) for no in output))


print("==================Output of Program1===========")
program1()


# Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name


def program2():
    first = input("Enter your first name : ")
    last = input("Enter your last name : ")
    print("{} {} ".format(last, first))


print("==================Output of Program2===========")
program2()

# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r^3


def program3():
    V = (4/3) * math.pi * math.pow(12, 3)
    print("Volume of a sphere with diameter 12 is:", V)


print("==================Output of Program3===========")
program3()
