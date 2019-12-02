def is_member(x,a:list):
    for i in a:
        if i == x:
            return True
    return False

print(is_member(5,[2,4,5]))