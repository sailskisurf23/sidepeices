test_str = "This is a test string"

result = ''
for i,char in enumerate(test_str):
    if i % 2 == 0:
        result += char.upper()
    else:
        result += char.lower()

print(result)
