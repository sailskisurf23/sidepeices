import numpy as np

def sum_pairs(ints, s):
    winners_inx = []
    for i,x in enumerate(ints):
        for j,x in enumerate(ints[i+1:]):
            if ints[i] + ints[i+j+1] == s:
                winners_inx.append((i,i+j+1))
    print (winners_inx)
    if len(winners_inx) == 0:
        return None
    m_list=np.zeros(len(winners_inx))
    for i,item in enumerate(winners_inx):
        m_list[i] = max(item[0],item[1])
    m_ind = np.argmin(m_list)
    return [ints[winners_inx[m_ind][0]], ints[winners_inx[m_ind][1]]]



l1= [1, 4, 8, 7, 3, 15, 1]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

print(sum_pairs(l1, 8)) #== [1, 7]
#print(sum_pairs(l2, -6)) # == [0, -6]
