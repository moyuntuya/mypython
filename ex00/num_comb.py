# 00 01, 00 02, 00 03, 00 04, 00 05, ..., 00 99, 01 02, 01 03, ..., 97 99, 98 99$

for i in range(0,99):
    for j in range(1,100):
        if i < j:
            result1 = i
            result2 = j
        #list_var.append(result2)
        #list_var.append(result1)
            #print('{num:02d}'.format(num = result1), end=" ")
            #print('{num:02d}'.format(num = result2), end=", ")
            print(format(result1, '02d'), end=" ")
            if i == 98:
                print(format(result2, '02d'), end="$")
            else:
                print(format(result2, '02d'), end=", ")

print(" \n")
# <012, 013, 014, 015, 016, 017, 018, 019, 023, ..., 789$>

list_var = []

for i in range(0,10):
    for j in range(0,10):
        for k in range (0,10):
            if i < j < k:
                result = (str(i) + str(j) + str(k))
                list_var.append(result)

print(list_var)

number_of_elements = len(list_var)
print(number_of_elements)

# 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20... 99

# Create an empty list variable
# loop 1st and 2nd digits
# Append the result in the list

list_var =[]

for i in range(0, 10):
    for j in range (0, 10):
        result = (str(i) + "" + str(j))
        #print(number, end=" ")
        list_var.append(result)

print(list_var)

number_of_elements = len(list_var)
print(number_of_elements)

# 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20... 98

list_var =[]

for i in range(0, 10):
    for j in range (0, 10):
        if i != j:
            result = (str(i) + "" + str(j))
            #print(number, end=" ")
            list_var.append(result)

print(list_var)

number_of_elements = len(list_var)
print(number_of_elements)

# 01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 20... 89

list_var =[]

for i in range(0, 10):
    for j in range (0, 10):
        if i < j:
            result = (str(i) + "" + str(j))
            #print(number, end=" ")
            list_var.append(result)

print(list_var)

number_of_elements = len(list_var)
print(number_of_elements)





