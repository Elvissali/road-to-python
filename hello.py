#import math
#a = 9.9
#b = 4.4 + 5.5
#c= a == b
#x1,x2= eval(input('Entry  ')) 
#x2 = eval(input('enty'))
#print('x1 =', x1, '\n' 'x2 =', x2 ,'\n' ,x1 + x2 )

#print('type in someting')
#x = input('enter\\\\') 
#print('you typed ',end="2")
#print(eval(input('try')))

#print('A', end='') # idk whats going on line 15-21
#print('B', end='')
#print('C', end='')
#print()
#print('X')
#print('Y')
#print('Z')

#w, x, y, z = 10, 15, 20, 25
#print(w, x, y, z)
#print(w, x, y, z, sep=',')
#print(w, x, y, z, sep='')
#print(w, x, y, z, sep=':') 
#print(w, x, y, z, sep='-----')

#a = 60
#b = 13
#c = a | b the >>,|,^, &,no idea
#print(c)

#x = 1001
#y = 1000 + 1
#print(id(x))
#print(id(y))

#a = 20
#b = 30
#c = (45 + 5) * 20
#print(c)

seconds = eval(input("Please enter the number of seconds:"))
# First, compute the number of hours in the given number of seconds
# Note: integer division with possible truncation
hours = seconds // 3600 # 3600 seconds = 1 hours
# Compute the remaining seconds after the hours are accounted for
seconds = seconds % 3600
# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // 60 # 60 seconds = 1 minute
# Compute the remaining seconds after the minutes are accounted for
seconds = seconds % 60
# Report the results
print(hours, "hr,", minutes, "min,", seconds, "sec")