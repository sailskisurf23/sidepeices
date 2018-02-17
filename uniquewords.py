#userinput = "enter comma-seperated list of words: "
userinput = 'hello, there, how, are, you, hello, you'
set1 = set([x.strip() for x in userinput.split(',')])
print(", ".join(set1))
