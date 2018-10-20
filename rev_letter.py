def reverse_letter(string):
    return ''.join([char for char in string[::-1] if char.isalpha()])


print(reverse_letter('krishan123'))


#Test.assert_equals(reverse_letter("krishan"),"nahsirk")
