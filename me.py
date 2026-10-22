rate=10
hours=input('enter hours worked\n')
hr=float(hours)
if hr<=40:
    pay=(hr * rate)
    print("your paycheck is", pay)
else:
    pay = (40 * rate) + ((hr - 40) * rate * 1.5)

    print('your paycheck is', pay)
