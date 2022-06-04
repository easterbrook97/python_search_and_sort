data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

target = int(input("please enter a target value"))

found = False

while found == False:
    search_point = round((len(data) - 1) / 2)

    if data[search_point] == target:
        print("value found")
        found = True
    elif target < data[search_point]:
        data = data[0:round((len(data) - 1) / 2)]
        print(data)
    elif target > data[search_point]:
        data = data[round((len(data)) / 2):len(data)]
        print(data)

print(data[search_point])


