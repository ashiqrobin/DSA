from stack import Stack

def reverse_str(str):
    s = Stack()
    a = ""
    for x in str:
        s.push(x)
    while not s.is_empty():
        a += s.pop()

    return a




    
