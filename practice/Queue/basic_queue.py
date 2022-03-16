def create_queue():
    queue = []
    return queue

def enqueue(queue, item):
    return queue.append(item)

def dequeue(queue):
    return queue.pop(0)

def isEmpty(queue):
    return True if len(queue)== 0 else False

def read(queue):
    for i in range(len(queue)):
        print(queue[i])

def peek(queue):
    return queue[0] 
