def sum_of_a_beach(beach):
    beach = beach.lower()
    beachlist = ['sand','sun','water','fish']
    count = 0
    idx = 0
    while idx < len(beachlist):
        if beach.find(beachlist[idx]) > -1:
            beach = beach.replace(beachlist[idx],'', 1)
            count += 1
            continue
        else:
            idx +=1
    return count


def sum_of_a_beach2(beach):
    beach = beach.lower()
    beachlist = ['sand','sun','water','fish']
    count = 0
    for word in beachlist:
        if word in beach:
            count += beach.count(word)
    return count




s1 = 'sunsunsunsunsand'
s2 = 'sandwaterfishlkadjg'

print(sum_of_a_beach2(s1))
