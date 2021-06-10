import re
#Increments last number in a string while keeping leading zeros
def increment_string(strng: str) -> str:
    x = re.findall('\d+\Z', strng)
    if x == []:
        strng = strng + '1'
    else:
        y = len(x[0])
        z = str(int(x[0])+1)
        strng = strng.replace(x[0], '0'*(y - len(z))+z)
    return strng


#Examples
#print(increment_string('foobar00'))
#print(increment_string('foobar'))
#print(increment_string('foobar00099'))
#print(increment_string('foobar8'))
