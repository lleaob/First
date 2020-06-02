#4 Operations Calculator


def chk_float(I):
    try:
        I = float(I)
    except ValueError:
        print("Not a valid input. ")
        return(False)
    else:
        return(True)

def chk_operator(I):
    if var3 == "+" or var3 == "-" or var3 == "*" or var3 == "/":
        return(True)
    else:
        print("Not a valid input.")
        return(False)

def chk_repeat(I):
    if I == "y" or I == "n":
        return(True)
    else:
        print("Not a valid input.")
        return(False)

repeat = "n"
var1 = 0
while repeat == "n":

    var1 = input("\nType 1st number ")
    while chk_float(var1) == False:
        var1 = input("\nType 1st number ")
    else:
        var1 = float(var1)
    
    var2 = input("\nType 2st number ")
    while chk_float(var2) == False:
        var2 = input("\nType 2st number ")
    else:
        var2 = float(var2)

    var3 = input("Type the operation: + - * / ")
    while chk_operator(var3) == False:
        var3 = input("Type the operation:  + - * / ")

    if var3 == "+":
        print(var1+var2)
    elif var3 == "-":
        print(var1-var2)
    elif var3 == "*":
        print(var1*var2)
    elif var3 == "/":
        if  var2 == 0:
            if var1 >= 0:
                print("\u221E")
            else:
                print("-\u221E")
        else:
            print(var1/var2)

    repeat = input("\nClose Calculator? (y or n) ")
    while chk_repeat(repeat) == False:
        repeat = input("\nClose Calculator? (y or n) ")