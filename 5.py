def overlapping (lst1:list,lst2:list):
    for i in lst1:
        for j in lst2:
            if i==j:
                return True

    return False

print(overlapping([2,3,4,5],[5,6,7,8]))