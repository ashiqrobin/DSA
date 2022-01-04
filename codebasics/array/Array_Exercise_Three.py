def input(max_num:int)->list:
    arr = []
    for i in range(1,max_num+1):
        if i%2 != 0:
            arr.append(i)
        else:
            continue
    return arr

