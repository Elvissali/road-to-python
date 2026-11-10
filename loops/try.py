# count = 0
# for i in [3, 41, 12, 9, 74, 15]:
#     count += 1
# print('Count:', count)

entry = 0
add = 0
print("Enter numbers to add, negative number ends list:")
while entry >= 0:
     entry = eval(input('>'))
     if entry >= 0:
         add += entry
print("added =",add)