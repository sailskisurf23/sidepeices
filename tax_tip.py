#2. Write a function that will calculate the total amount of a dinner bill,
#given the total before tax, the tax rate, and the tip percentage.
#Your function will accept these three values as arguments. It will then do the following:

 #* Apply the tax rate to the bill total.
 #* Apply the tip percentage to the total amount.
 #* Return the total amount of bill before and after tip.

userinput1 = float(input("Input Bill Amount: "))
userinput2 = float(input("Input Tip Rate: "))
userinput3 = float(input("Input Tax Rate: "))


def tax_tip(billamt, tiprate, taxrate):
    tipamt = billamt * tiprate
    taxamt = billamt * taxrate
    total = billamt + tipamt + taxamt
    return billamt,total

a,b = tax_tip(userinput1,userinput2,userinput3)

print(f"The bill before tax was {a}. \nThe bill after tax is {b}")
