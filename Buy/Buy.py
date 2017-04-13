# THIS DOES NOT WORK IF YOU FIX IT EMAIL IT TO US AT KILLIAN@REDSTONERMOVES.COM THANK YOU!
# hello!
print("BY HTTP://WWW.REDSTONERMOVES.COM/")
money = input("how much $$$ you have (DO NOT PUT THE $ SIGN!!!) ")
maxMoney = 10
if money < maxMoney:
    money = maxMoney - 3
    print("Oh no! you put to much! we have set your money to $" + (maxMoney - 3) + " sorry!")
buy1Price = 3
buy1 = input("Do you want a meal for " + buy1Price + "? [y or n]")
if buy1 == "y":
    money = money - buy1Price
    print("DONE YOU NOW HAVE $" + money + "!")
# DO NOT REMOVE LINES 2 & 13 THANK YOU
