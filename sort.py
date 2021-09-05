# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
list1 = []
while True:
    element = int(input("enter the element"))
    list1.append(element)
    choice = input("want to stop? if yes press yes otherwise press any key!")
    if choice == "yes":
        break
from statistics import pstdev
def ascending_sort(list1):
    list2 = []
    while list1:
        min = list1[0]
        for i in list1:
            if i < min:
                min = i
        list2.append(min)
        list1.remove(min)
    return list2
print(ascending_sort(list1))


