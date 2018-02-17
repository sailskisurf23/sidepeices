def game(a, b):
    if a == 0 or b == 0:
        return "Non-drinkers can't play"
    beerstodrink = 1
    mikecount = 0
    joecount = 0
    while True:
        if beerstodrink % 2 != 0:
            mikecount += beerstodrink
            beerstodrink += 1
            if mikecount > a:
                return "Joe"
        if beerstodrink % 2 == 0:
            joecount += beerstodrink
            beerstodrink += 1
            if joecount > b:
                return "Mike"
    else:
        return "broken"

print(game(4,5))
