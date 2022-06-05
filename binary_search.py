data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

temp_data = data

target = int(input("please enter a target value"))

found = False

while found == False:
    search_point = round((len(temp_data) - 1) / 2)

    if temp_data[search_point] == target:
        print("value found")
        found = True
    elif target < temp_data[search_point]:
        temp_data = temp_data[0:round((len(temp_data) - 1) / 2)]
        print(temp_data)
    elif target > temp_data[search_point]:
        temp_data = temp_data[round((len(temp_data)) / 2):len(temp_data)]
        print(temp_data)


