def make_forming(verb:str):
    special = ["be","see","flee","knee"]
    consonant = "bcdfghjklmnpqrstvwxyz"
    vowel = "aiueo"
    if verb[-2:] == "ie":
        verb = verb[:-2] + "ying"
        return verb
    if verb[-1] == "e" and verb not in special:
        verb = verb[:-1] + "ing"
        return verb
    if consonant.find(verb[-3]) != -1:
        if vowel.find(verb[-2]) != -1:
            if consonant.find(verb[-1]) != -1:
                verb = verb + verb[-1] + "ing"
                return verb

    return verb+"ing"

print(make_forming("fhloc"))
    