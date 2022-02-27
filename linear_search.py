lst = [1,2,3,4,5]

def linear(searchval):
    for i in lst:
        if i == searchval:
            print("yay I found", searchval)


linear(5)