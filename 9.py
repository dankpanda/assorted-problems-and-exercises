def filter_long_words(lwords:list, n=int):
    display:list = []
    for i in lwords:
        if len(i)> n:
            display.append(i)

    return(display)

print(filter_long_words(["joj","dobb","rayster","s"],4))