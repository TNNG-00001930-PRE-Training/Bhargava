# Problem - 1
'''res = []
for num in range(2000, 3201):
    if num % 7 == 0:
        if num %2 != 0:
            res += [str(num)]
temp = ','.join(res)
print(temp)'''

# Problem - 2
'''res = {}
n = int(input('Enter a range of a number : '))
for i in range(1, n + 1):
    res[i] = i*i

print(res)'''

# Problem - 3

'''n = input('Enter comma-seperated integers : ')
n = n.split(',')
print(n)
print(tuple(n))'''

# Problem - 4

'''class A:
    def getString(self):
        self.string = input('Enter a String : ')
    def printString(self):
        print(f'Modified string : {self.string.upper()}')

def test_function():
    res = A()
    res.getString()
    res.printString()

test_function()'''

# Problem - 5

'''string = input('Enter comma-seperated words : ')
L = string.split(',')
L.sort()
print(L)'''

# Problem - 6

'''string = input('Enter a string : ')
L = string.split()
L = list(set(L))
res = sorted(L)
print(' '.join(res))'''

# Problem - 7

'''res = []
for num in range(1000, 3001):
    if all( int(digit)%2 == 0 for digit in str(num)):
        res.append(str(num))
print(','.join(res))'''

# Problem - 8

'''string = 'Hello world!'
upper = 0
lower = 0
for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    else:
        continue
print(f'Upper letters in the string is : {upper}')
print(f'Lower letters in the string is : {lower}')'''

# Problem - 9

'''import re

def check_password(Pass):
    if len(Pass) < 6 or len(Pass) > 12:
        return False
        
    if (not re.search("[a-z]", Pass)) or (not re.search("[A-Z]", Pass)) or (not re.search("[0-9]", Pass)) or (not re.search("[$#@]", Pass)):
        return False

    else:
        return True

Pass = input("Enter the password: ")
if check_password(Pass):
    print("Password is valid....")
else:
    print("Password is invalid....")'''

# Problem - 10

'''import re

def check_password(Pass):
    if len(Pass) < 6 or len(Pass) > 12:
        return False

    if not re.search("[a-z]", Pass) or (not re.search("[A-Z]", Pass)) or (not re.search("[0-9]", Pass)) or (not re.search("[$#@]", Pass)):
        return False
        
    return True

Pass = input("Enter comma-separated passwords: ")
L = Pass.split(',')
res = []

for Pass in L:
    if check_password(Pass):
        res.append(Pass)

output = ','.join(res)
print(output)
'''