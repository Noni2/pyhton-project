# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
list1 = []
while True:
    element = int(input("enter the element"))
    list1.append(element)
    choice = input("want to stop? if yes press yes otherwise press sny key!")
    if choice == "yes":
        break
from statistics import pstdev
def mean_and_std(list1):
    sum = 0
    for i in list1:
        sum +=i
    mean = sum/len(list1)

    std = pstdev(list1)

    return "mean - %s" %(mean) +"\n" + "STD - %s" % (std)
print(mean_and_std(list1))
