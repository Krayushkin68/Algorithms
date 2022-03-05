from DataStructures.queue import Queue


def hot_potato_play(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)

    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()


if __name__ == '__main__':
    print(hot_potato_play(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 256))
