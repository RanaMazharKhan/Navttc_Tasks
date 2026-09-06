
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")
    
age = 28
while age > 19:
    print('Infinite Loop')
    break

i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1
    
a = 'geeksforgeeks'
i = 0
while i < len(a):
    i += 1
    pass
  
print('Value of i :', i)

def printInDecreasing(x):
    while (x >= 1):

        x -= 1
        print(x)

printInDecreasing(5)