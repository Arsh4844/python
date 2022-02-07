

charter_name = "ARNOLD'S AMAZING EATS"
print("                                           _____________________________________________")
print("                                          |                                             |")
print("                                          |                                             |")
print("                                          |            " + charter_name +  "            |")
print("                                          |                                             |")
print("                                          |_____________________________________________|")
print("")
print("                                          Welcome to our " + charter_name +  " restraunt")
print("")
print("                                we are starting our own ordering system for our staff and customers ")

food = ["Burger","Kebab"] 
price = ["$5", "$8"]
a = 0
b = 1
myorderfood=[]
myodercost=[]
counter=0


order = input("Can I take your order?\n y/n ")
if order == "No":
    exit()
else:
    print(" a)Burger = $5 \n b)Kebab = $8")


nextorder = True
while nextorder == True:

    foodorder = input("Please select item a or b ")

    if foodorder =="a":
        myorderfood.append(food[0])
        myodercost.append(price[0])
        counter=counter+1
        

    elif foodorder =="b":
        myorderfood.append(food[1])
        myodercost.append(price[1])
        counter=counter+1
        
    else:
        print("not on menu")
        
    print(myorderfood)
    print(myodercost)
    
    finished = input("Anything else y/n ")
    if finished == "y":
        nextorder = True
    else:
        nextorder = False


y = 0
print("")
print("   Here is your order.")
print("")
print("***************************")
while y<counter:
    print("Selected Item: " + (myorderfood[y]))
    print("Order cost: " +(myodercost[y]))
    y=y+1


confirm_order = input("Do you want to confirm the order y/n ")
if confirm_order == "n":
    exit()

else:
    coupon = input("If you are a student apply for student discount for 10% y/n. ")
    deliverytype = input(" Home Delivery y/n ")
    if deliverytype == "y" :

        print("Please enter your delivery details ")

        firstname = input("First name - ")
        lastname =input ("_Last name - ")
        print("Full delivery address")
        streetname = input("Street name - ")
        housenumber = input("House number - ") 
        unit =  input("Unit # if applicable (leave blank if none) - ")
        city = input("City - ")
        province = input("Province - ")
        postalcode = input("Postal Code - ")
        specialinstructions = input("Special Instruction for Delivery from this Address")
        phonenumber = input("Phone Number - ")
    else:
        print("Please enter your pickup details ")

        firstname = input("First name - ")
        lastname = input("_Last name - ")
        phonenumber = input("Phone Number - ")

print("Your Order is Succesfully")


print("                             ----------------------------------------------------------------------------------")
print("                             |                           ARNOLD'S AMAZING EATS                                |")
print("                             |                                 INVOICE                                        |")
print("                             |  " + firstname +  lastname + "                                                 |")
print("                             |  " + streetname + housenumber + unit + "                                       |")
print("                             |  " + city + province + postalcode + "                                          |")
print("                             |  " + specialinstructions + "                                                   |")
print("                             |                                                                                |")
print("                             |    Order                           Item Price                  Total           |")
print("                             |   -------------------            ----------------           -----------------  |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             |                                                                                |")
print("                             ----------------------------------------------------------------------------------") 


