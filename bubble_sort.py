data = [33, 3, 44, 5, 6, 7, 83, 9, 1001, 110]
temp = 0
swap_flag = True

while swap_flag == True:
    swap_flag = False
    for i in range(0, len(data) - 1):
        if data[i] > data[i + 1]:
            temp = data[i + 1]
            data[i + 1] = data[i]
            data[i] = temp
            swap_flag = True

print(data)
