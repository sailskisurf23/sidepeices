start_amt = int(input("How much money will you invest? Enter integer:"))
return_rate = float(input("What is your expected annual return? Enter a decimal between 0 and 1:"))
time = int(input("For how many years will you be invested? Enter integer:"))
counter = 0

while counter < time:
    counter = counter + 1
    start_amt = start_amt + return_rate * start_amt

start_amt = round(start_amt,2)

print("After " + str(time) + " years, you will have: $" + str(start_amt))
