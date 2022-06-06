from stack import Stack

def is_match(p1:str, p2:str) -> bool:
    """
    This methods checks two inputs
    are same or not

    Parameters
    ----------
    p1 : str
        first parentheses
    p2 : str
        second parentheses

    Returns
    -------
    bool
        if match it will return True
        otherwise False
    """
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paran_balance(brakets)->bool:
    """
    check brakets is balanced or not

    Parameters
    ----------
    brakets : str
        brackets

    Returns
    -------
    bool
        if balance return True 
        otherwise False
    """
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(brakets) and is_balanced:
        paren = brakets[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break                
            else:
                top = s.pop()
                if not is_match(top,paren): 
                    is_balanced = False
                    break
        index += 1



    if s.is_empty() and is_balanced:
        return True
    else:
        return False    


    

