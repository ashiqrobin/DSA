"""Implementing Stack Data Structure 
"""

from typing import Union

def create_stack()->list:
    """It creates an empty stack

    Returns
    -------
    list
        empty list
    """
    stack = []
    return stack

def isEmpty(stack:list)->bool:
    """check the stack length

    Parameters
    ----------
    stack : list
        stack is a list
    Returns
    -------
    bool
        if length zero it will return true
        otherwise false
    """
    return True if len(stack)== 0 else False

def push(stack:list, item:Union[int,str])->list:
    """Add data to stack

    Parameters
    ----------
    stack : list
        stack is a list
    item : Union[int,str]
        items to add to stack

    Returns
    -------
    list
        updated stack
    """
    return stack.append(item)

def popout(stack:list)->Union[list,str]:
    """remove data from stack

    Parameters
    ----------
    stack : list
        stack is a list

    Returns
    -------
    Union[list,str]
        if there is no data it will return string
        if it removes data it will return updated stack
    """
    if isEmpty(stack):
        return "No Data is available"
    return stack.pop()
def read(stack:list):
    """Present the whole data stack

    Parameters
    ----------
    stack : list
        stack is a list
    """
    for i in range(len(stack)):
        print(stack[i])

def peek(stack:list):
    """Return the last value of the stack
    without removing that

    Parameters
    ----------
    stack : list
        stack is a list
    """
    print(stack[len(stack)-1])



