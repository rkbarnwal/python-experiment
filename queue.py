class Queue:
    def __init__(self):
        self.__queue = []

    def isEmpty(self):
        return len(self.__queue) == 0

    def push(self, object):
        self.__queue.append(object)

    def pop(self):
        if self.isEmpty():
            return 0
        else:
            return self.__queue.pop(0)

    def peek(self):
        return self.__queue[0]

    def size(self):
        return len(self.__queue)

    def search(self, object1):
        return self.__queue.index(object1)


