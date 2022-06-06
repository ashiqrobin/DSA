from stack import Stack

def convert(value):
    s = Stack()
    x = ""
    while value > 0:
        if value % 2 == 0:
            s.push("0")
        else:
            s.push("1")
        value = value//2

    while not s.is_empty():
        x += s.pop()

    return int(x)
