CALCULATOR
def calculate():
    try:
        a = int(input("enter a"))
        b = int(input("enter b"))
        print("my calculator program")
        list1 = ['add', 'sub', 'mul', 'div']
        print(list1)
        i = 0
        while i < 2:
            opt = input("enter option in list")
            if opt not in list1:
                print("you entered wrong option")
                i += 1
                if i < 2:
                    print('please try again')
                elif i == 2:
                    print("your tries over")
		    again()
            else:
                if opt == 'add':
                    add = a + b
                    print("%d+%d is %d " % (a, b, add))
                    again()
                    break

                elif opt == 'sub':
                    sub = a - b
                    print("%d-%d is %d" % (a, b, sub))
                    again()
                    break

                elif opt == 'mul':
                    mul = a * b
                    print("%d * %d is %d" % (a, b, mul))
                    again()
                    break

                else:
                    div = a / b
                    print("%d/%d is %0.3f" % (a, b, div))
                    again()
                    break

                print("thanks for using my calculator")

    except ValueError as err1:
        print(err1)
        again()
    except ZeroDivisionError as err2:
        print(err2)
        again()

def again():
    calc_again=input("Do you want to continue again?Please type Y for YES or N for NO")
    if calc_again.upper()=='Y':
        calculate()
    elif calc_again.upper()=='N':
        print("bye")
    else:
        again()

calculate()