def char_freq(text:str):
    data:dict = {}
    for i in text:
        if i not in data.keys():
            data[i] = 1
        else:
            data[i] += 1
    return data

print(char_freq("Hello"))