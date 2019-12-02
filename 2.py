def translate(text):
    vowel = ['a','o','i','u','e',' ']
    sentence = ""
    for i in text:
        sentence += i
        if i not in vowel:
            sentence += "o" + i
    return sentence

print(translate("this is fun"))
    