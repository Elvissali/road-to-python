rate=10
hours=input('enter hours worked\n')
hr=float(hours)
def computepay(hr,rate):
    dn = hr * rate
    return dn

if hr<=40:
    pay= computepay(hr,rate)
    print("your paycheck is", pay)
else:
    pay = computepay(40,rate) + (computepay((hr - 40) , rate) * 1.5)

    print('your paycheck is', pay)
    #its for counting pay an employee gets for hours worked but if the employee works over 40hrs gets 1.5 for overtime worked
