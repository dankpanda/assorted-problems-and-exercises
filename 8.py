def find_longest_word(lword:list):
    length_value = []
    for i in lword:
        length_value.append(len(i))
    length_value.sort()
    for i in lword:
        if max(length_value)==len(i):
            return i
            
    return "There are two or more elements with equal amount of characters"
        

print(find_longest_word(["hello","hieee","xdo"]))


