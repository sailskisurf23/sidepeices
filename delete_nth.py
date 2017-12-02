userlist = input("Input Comma Separated List (No []) : ").split(",")
usermax = int(input("Input Max Occurences: "))

def delete_nth(order,max_e):
    newlist = []
    for x in range(len(order)):
        itemcount = order[:x+1].count(order[x])
        if itemcount <= max_e:
            newlist.append(order[x])
    return newlist

print(delete_nth(userlist,usermax))
