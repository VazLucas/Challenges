name = str(input('Type a name:'))
convertedName = ''
for i in name:
    if (i == 'a' or i == 'A'):
        convertedName += '@'
    elif (i == 'e' or i == 'E'):
        convertedName += '&'
    elif (i == 'o' or i == 'O'):
        convertedName += '#'
    elif (i == 'i' or i == 'I'):
        convertedName += '!'
    elif (i == 'u' or i == 'U'):
        convertedName += '*'
    else:
        convertedName += i
print(convertedName.upper())
