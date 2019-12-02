def make_forms(verb:str):
    a = ["o","ch","s","sh","x","z"]
    if verb[-1] == 'y':
        verb = verb[:-1]+"ies"
        return verb
    if verb[-1] in a or verb[-2] in a:
        verb = verb + "es"
        return verb
    if verb[-1] != 'y' and verb[-1] not in a and verb[-2] not in a:
        verb = verb + 's'
        return verb

print(make_forms("try"))
print(make_forms("run"))
print(make_forms("brush"))
print(make_forms("fix"))

    