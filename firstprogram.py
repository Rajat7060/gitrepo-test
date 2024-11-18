#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RAJAT
#
# Created:     16-08-2024
# Copyright:   (c) RAJAT 2024
# Licence:     <you
first=int(input("enter first numder :"))
operator = (input("enter operator (+,-,*,/,%):"))
second = int(input("enter second number :"))

if operator=="+":
    print(first + second)
elif operator=="-":
    print(first - second)
elif operator=="*":
    print(first * second)
elif operator=="/":
    print(first / second)
elif operator=="%":
    print(first % second)
else:
    print("invalid operation")