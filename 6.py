# 6)Write a Python program to implement a queue using a list. (enqueue and dequeue)


queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print("Queue after enqueuing 1, 2, and 3:", queue)

#dequeue
if queue:
    dequeued_item = queue.pop(0)
    print("Dequeued item:", dequeued_item)
else:
    print("Queue is empty. Cannot dequeue.")

print("Queue after dequeuing:", queue)

# Enqueue
queue.append(4)
print("Queue after enqueuing 4:", queue)

# Peek at the front element without removing it
if queue:
    front_item = queue[0]
    print("Front item:", front_item)
else:
    print("Queue is empty. Cannot peek.")

print("Size of the queue:", len(queue))
