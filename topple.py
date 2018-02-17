def will_it_balance(stick, terrain):
    com = sum([x*y for x,y in enumerate(stick)]) / sum(stick)
    safe_range_l = min([i for i,x in enumerate(terrain) if x == 1])
    safe_range_r = max([i for i,x in enumerate(terrain) if x == 1])
    return com >= safe_range_l and com <= safe_range_r


stick1 = [2,3,2,2]
terrain1 = [0,1,1,0]

print(will_it_balance(stick1,terrain1))

#Test.assert_equals(will_it_balance([2,3,2],[0,1,0]), True)
#Test.assert_equals(will_it_balance([5,1,1],[0,1,0]), False)
#Test.assert_equals(will_it_balance([3,3,4],[0,1,0]), False)
