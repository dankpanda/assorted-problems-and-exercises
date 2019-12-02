def list_tuple():
    data = input("Enter comma separated values: ")
    list_value = []
    data_split=data.split(",")
    print("Output:")
    print("List:",data_split)
    print("Tuple:",tuple(data_split))

list_tuple()