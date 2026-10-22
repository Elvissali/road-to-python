print('Hello its Elvis')
gender = input('What is your gender? ')

if gender.lower() == 'male':
    print('man get your ass out of here')

elif gender.lower() == 'female':
    ask = input('Are you free tonight? ')

    if ask.lower() == 'yes':
        print('Come to my place')
    else:
        print(ask)

else:
    print("Let's be with common sense")
