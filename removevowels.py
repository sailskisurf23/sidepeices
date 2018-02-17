s = 'hello world'

vowels = ['a','e','i','o','u','A','E','I','O','U']
result = ''.join([x for x in s if x not in vowels])

print(result)
