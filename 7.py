def mapping(text:list):
    number_list = []
    for i in range(len(text)):
        number_list.append(len(text[i]))

    return number_list

print(mapping(["hello","house","dog"]))
