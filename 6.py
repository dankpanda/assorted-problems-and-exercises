def histogram(lst:list):
    lst_bar = []
    for i in range(len(lst)-1):
        print("*" * lst[i])

print(histogram([2,3,4,5]))