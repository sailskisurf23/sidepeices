#userinput1 = input("enter comma-separated list: ")
#userinput2 = input("enter comma-separated list: ")

userinput1 = '1, 2, 3, 4'
userinput2 = '3, 4, 5, 6'

l1 = [int(x) for x in userinput1.split(',')]
l2 = [int(x) for x in userinput2.split(',')]
common = [x for x in l1 if x in l2]
result = str(common).strip("[]")
print(result)
