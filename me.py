# rate=10
# hours=input('enter hours worked\n')
# hr=float(hours)
# if hr<=40:
#     pay=(hr * rate)
#     print("your paycheck is", pay)
# else:
#     pay = (40 * rate) + ((hr - 40) * rate * 1.5)

#     print('your paycheck is', pay)
# pwd = '1234'
# user= 'elvis'

# print('login')
# user_name = input('enter username\n')
# password = input('enter password\n')
# if user_name == user and password == pwd:
#     print('user found')
#     print('welcome',user)
# else:
#     print('wrong username or password')
    
# d1= 1.11 - 1.10
# d2=2.11 - 2.10
# print('d1 =',d1,'d2 =',d2)


# print("Help! My computer doesn't work")
# print("Does the computer make any sounds (fans, etc.)")               #nested if/else
# choice = input("or show any lights? (y/n):")
# if choice =='n':
#     choice = input("Is it plugged in? (y/n):")
#     if choice =='n':
#         print("plug it in. If the problem persists, ")
#         print("please run this program again.")
#     else:
#         choice = input("Is the switch in the \"on\" position? (y/n):")
#         if choice == 'n':
#             print("Turn it on. If the problem persists,")
#             print("please run this program again.")
#         else:
#             choice = input("Does tje computer have a fuse? (y/n):")
#             if choice == 'n':
#                 choice = input("Is the outlet's OK? (y/n)")
#                 if choice == 'n':
#                     print("Check the outlet's circuit")
#                     print("btraker or fuse. Move to a")
#                     print("new outlet, if necessary.")
#                     print("If the problem persists")
#                     print("Please run this program again.")
#                 else:
#                     print("Please consult a service technician.")
#             else:
#                 print("Check the fuse. Replace if")
#                 print("necessary. If the problem")
#                 print("persists,then")
#                 print("Please run this program again.")
# else:
#     print("Please consult a service technician.")

n = eval(input("Entex a number: "))
print('|' , n, ' | = ' , (-n if n < 0 else n), sep="")
