total = 0
count = 0

while True:
    user_input = input("Enter a number: ")

    if user_input.strip().lower() == "done":
        break

    try:
        number = int(user_input)
        total += number
        count += count + 1
    except ValueError:
        print("Invalid input")
        continue

if count > 0:
    average = total / count
    print(total, count, average)
else:
    print("No numbers were entered.")
