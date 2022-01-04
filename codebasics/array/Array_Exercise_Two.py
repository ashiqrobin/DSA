heros=['spider man','thor','hulk','iron man','captain america']

def lenth(heros:list)->int:
    count = 0
    for _ in heros:
        count += 1
    return count

def addapp(value:str)->list:
    heros.append(value)
    return heros

def rmv(value:str)->list:
    heros.remove(value)
    return heros

def indx(value:str)->int:
    for i in range(len(heros)):
        if heros[i] == value:
            return i
        else:
            continue
    return "not found"

def srt(value:list)->list:
    l = value.sort()
    return l
