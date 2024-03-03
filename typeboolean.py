# Check if variable is a word or number

word = "hi"
digit = 7.9
notfloat = 3

print("---------String----------")
# Check for string

print(type(word) == str) #True
print(type(digit) == str) #False    

print("---------Integer & Float----------")
# Check for integer (including float)

print(type(word) == int) #False
print(type(digit) == int) #False
print(type(digit) == float) #True
print(type(notfloat) == float) #False
print(type(notfloat) == int) #True