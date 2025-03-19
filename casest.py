# num=0
# match num:
#     case 0:
#         print("it is zero")
#     case 1:
#         print("it is non zero")
#     case _:
#         print("invalid")

month=int(input("enter the number of month: "))
match month:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("august")
    case 9:
        print("september")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
        print("december")
    case _:
        print("invalid month number")


