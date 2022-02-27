print("Welcome to Unit Converter")
converter = ["length","weight"]
inputnumber = ["1","2"]
length = 1
weight = 2
print("What do you want to convert")
command = input(" length \n weight \n:-")
if command == "length":
    print("You have selected length")
    lengthinput = input("Please enter lenght: ")
    lengthunit = input("Please Enter current unit \n feet \n meter \n :")
    if lengthunit == "meter":
        resultinfeet = float(lengthinput) / float(0.304)
        print("Result in feet:")
        print(resultinfeet)
    elif lengthunit == "feet":
        resultinmeter = float(lengthinput) * float(0.304)
        print("Result in meter:")
        print(resultinmeter)
    else: exit()
elif command == "weight":
    print("You have selected weight")   
    weightinput = input("please enter weight: ")
    weightunit = input("Please Enter current unit \n kg \n lbs \n :")
    if weightunit == "kg":
        resultinlbs = float(weightinput) * float(2.2)
        print("Result in lbs")
        print(resultinlbs)
    elif weightunit == "lbs":
        resultinkg = float(weightinput) / float(2.2)
        print("Result in kg")
        print(resultinkg)
    else: exit()
else: exit() 