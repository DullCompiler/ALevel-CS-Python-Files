#stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

#queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    def size(self):
        return len(self.items)


stack = Stack()
queue = Queue()

while True:
    #gives choices for initialization
    print("""Stack: S
Queue: Q
Exit: E""")

    #gets input and validates
    choice = input("Selection: ").lower()
    if choice == "s":
        choice = "stack"
    elif choice == "q":
        choice = "queue"
    elif choice == "e":
        break
    else:
        print("Please provide a valid input")
        continue

    #stack actions
    if choice == "stack":
        leave = False
        while not leave:
            print("""Enter the phrases to use stack:
                push
                pop
                peek
                isempty
                size
                *insert another phrase to exit*""")
            action = input("Choice: ").lower()
            if action == "push":
                item = input("Enter Value: ")
                stack.push(item)
            elif action == "pop":
                stack.pop()
            elif action == "peek":
                stack.peek()
            elif action == "isempty":
                stack.is_empty()
            elif action == "size":
                stack.size()
            else:
                leave = True

    #queue actions
    if choice == "queue":
        leave = False
        while not leave:
            print("""Enter the phrases to use queue:
                enqueue
                dequeue
                peek
                isempty
                size
                *insert another phrase to exit*""")
            action = input("Choice: ").lower()
            if action == "enqueue":
                item = input("Enter Value: ")
                queue.enqueue(item)
            elif action == "dequeue":
                queue.dequeue()
            elif action == "peek":
                queue.peek()
            elif action == "isempty":
                queue.is_empty()
            elif action == "size":
                queue.size()
            else:
                leave = True