string = "159"
string = string.lower()
print(string)
string = list(string)
for i in string:
    if i == " ":
        string.remove(i)
print(string)

# . = x
# _ = o
for i in range(len(string)):
    if string[i] == 'a':
        string[i] = '._'

    elif string[i] == 'b':
        string[i] = '_...'

    elif string[i] == 'c':
        string[i] = '_._.'

    elif string[i] == 'd':
        string[i] = '_..'

    elif string[i] == 'e':
        string[i] = '.'
    
    elif string[i] == 'f':
        string[i] = '.._.'

    elif string[i] == 'g':
        string[i] = '__.'

    elif string[i] == 'h':
        string[i] = '....'

    elif string[i] == 'i':
        string[i] = '..'

    elif string[i] == 'j':
        string[i] = '.___'

    elif string[i] == 'k':
        string[i] = '_._'

    elif string[i] == 'l':
        string[i] = '._..'

    elif string[i] == 'm':
        string[i] = '__'

    elif string[i] == 'n':
        string[i] = '_.'

    elif string[i] == 'o':
        string[i] = '___'

    elif string[i] == 'p':
        string[i] = '.__.'

    elif string[i] == 'q':
        string[i] = '__._'

    elif string[i] == 'r':
        string[i] = '._.'

    elif string[i] == 's':
        string[i] = '...'

    elif string[i] == 't':
        string[i] = '_'

    elif string[i] == 'u':
        string[i] = '.._'

    elif string[i] == 'v':
        string[i] = '..._'

    elif string[i] == 'w':
        string[i] = '.__'

    elif string[i] == 'x':
        string[i] = '_.._'

    elif string[i] == 'y':
        string[i] = '_.__'

    elif string[i] == 'z':
        string[i] = '__..'

    elif string[i] == '0':
        string[i] = '_____'

    elif string[i] == '1':
        string[i] = '.____'

    elif string[i] == '2':
        string[i] = '..___'

    elif string[i] == '3':
        string[i] = '...__'

    elif string[i] == '4':
        string[i] = '...._'

    elif string[i] == '5':
        string[i] = '.....'

    elif string[i] == '6':
        string[i] = '_....'

    elif string[i] == '7':
        string[i] = '__...'

    elif string[i] == '8':
        string[i] = '___..'

    elif string[i] == '9':
        string[i] = '____.'

    else:
        string[i] = 'x'

print(string)
#code = [i.split(' ')[0] for i in string] 
#for i in string:
#    string[i].split
code = ""
code = code.join(string)
code = list(code)
print(code)

newCode="".join([str(i) for i in code])
print(newCode)

txt = newCode[::-1]
print(txt)

if newCode == txt:
    answer = 1
else:
    answer = 0