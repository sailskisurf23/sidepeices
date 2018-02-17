s = 'hello world'
result = ''
for x in range(len(s)):
    if x % 2 == 0:
        result += s[x].lower()
    if x % 2 != 0:
        result += s[x].upper()

print(result)
