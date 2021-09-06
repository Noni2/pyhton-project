tele_book = { 1111111111:"Amal",
              2222222222: "Mohammed",
              3333333333: "Khadijah",
              4444444444: "Abdullah",
              5555555555:"Rawan",
              6666666666:"Faisal",
              7777777777:"Layla"}


def foo(val, dic):
    for key, value in dic.items():
        if val == value:
            return key

while True:
     choice = input("to search by number press b , to search by names press n, if want add new number press any key")
     if choice == "b":
         number = int(input('enter the number'))
         if len(str(number)) ==10:
           if number in tele_book:
              print(tele_book[number])
           else:
               print("Sorry, the number is not found")
         else:
            print("This is invalid number")
     elif choice == "n":
         name = input("enter the name")
         a = foo(name ,tele_book)
         print(a)
     else:
         new_number = int(input("enter the new number"))
         new_name = input("enter the name")
         tele_book[new_number] = new_name

