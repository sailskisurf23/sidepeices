#Solve the equation below:
#(a + (b - c) * d - e) * f = 75
#each integer is a unique integer between 1 and 6

for a in range(1,7):
    for b in range (1,7):
        for c in range (1,7):
            for d in range (1,7):
                for e in range (1,7):
                    for f in range (1,7):
                        if ((a not in [b,c,d,e,f]) and
                        (b not in [a,c,d,e,f]) and
                        (c not in [b,a,d,e,f]) and
                        (d not in [b,c,a,e,f]) and
                        (e not in [b,c,d,a,f]) and
                        (f not in [b,c,d,e,a]) and
                        ((a + (b - c) * d - e) * f == 75)):
                            print("The solution to '(a + (b - c) * d - e) * f = 75' is: \n" +
                            "a = "+ str(a) + ", " + "\n"
                            "b = "+ str(b) + ", " + "\n"
                            "c = "+ str(c) + ", " + "\n"
                            "d = "+ str(d) + ", " + "\n"
                            "e = "+ str(e) + ", " + "\n"
                            "f = "+ str(f))
