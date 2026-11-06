# rate=10
# hours=input('enter hours worked\n')
# hr=float(hours)
# if hr<=40:
#     pay=(hr * rate)
#     print("your paycheck is", pay)
# else:
#     pay = (40 * rate) + ((hr - 40) * rate * 1.5)

#     print('your paycheck is', pay)
pwd = '1234'
user= 'elvis'

print('login')
user_name = input('enter username\n')
password = input('enter password\n')
if user_name == user and password == pwd:
    print('user found')
    print('welcome',user)
else:
    print('wrong username or password')
    


