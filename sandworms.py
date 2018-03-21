import math

def harvester_rescue(data):
	#your code goes here. you can do it!
    d_worm_xy = [a - b for a,b in zip(data['harvester'], data['worm'][0])]
    d_worm = math.sqrt(d_worm_xy[0]**2 + d_worm_xy[1]**2)
    t_worm = d_worm / data['worm'][1]

    d_carry_xy = [a - b for a,b in zip(data['harvester'], data['carryall'][0])]
    d_carry = math.sqrt(d_carry_xy[0]**2 + d_carry_xy[1]**2)
    t_carry = d_carry / data['carryall'][1] + 1

    return t_worm, t_carry

    if t_carry < t_worm: return 'The spice must flow! Rescue the harvester!'
    else: return 'Damn the spice! I\'ll rescue the miners!'


data1 = {'harvester': [200,400], 'worm': [[200,0],40], 'carryall': [[500,100],45]}

print(harvester_rescue(data1))




# test.describe('Example Tests')
# data1 = {'harvester': [345,600], 'worm': [[200,100],25], 'carryall': [[350,200],32]}
# data2 = {'harvester': [200,400], 'worm': [[200,0],40], 'carryall': [[500,100],45]}
# data3 = {'harvester': [850,125], 'worm': [[80,650],20], 'carryall': [[80,600],20]}
# data4 = {'harvester': [0,320], 'worm': [[250,680],42], 'carryall': [[550,790],58]}
# data5 = {'harvester': [0,0], 'worm': [[0,600],50], 'carryall': [[0,880],80]}
#
# Test.assert_equals(harvester_rescue(data1),'The spice must flow! Rescue the harvester!')
# Test.assert_equals(harvester_rescue(data2),'Damn the spice! I\'ll rescue the miners!')
# Test.assert_equals(harvester_rescue(data3),'The spice must flow! Rescue the harvester!')
# Test.assert_equals(harvester_rescue(data4),'Damn the spice! I\'ll rescue the miners!')
# Test.assert_equals(harvester_rescue(data5),'Damn the spice! I\'ll rescue the miners!')
