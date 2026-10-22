
inp=input('enter score')
try:
    marks=float(inp)
except:
    print('bad score')
    quit() #so when put letters it stops here

if marks >=0.9:
    print('A')
elif marks >= 0.8:
    print('B')
elif marks >= 0.7:
    print('C')
elif marks >= 0.6:
    print('D')
elif marks < 0.6:
    print('F')
else:
    print('bad score')