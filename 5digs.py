def solution(digits):
    sol_list = []
    for x in range(len(digits)-4):
        sol_list.append(int(digits[x] + digits[x+1] + digits[x+2] +digits[x+3] + digits[x+4]))
    return max(sol_list)

userinput = input("Digits: ")
print(solution(userinput))
