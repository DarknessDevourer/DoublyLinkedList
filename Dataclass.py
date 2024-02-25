from dataclasses import dataclass


@dataclass
class Node:
    value: any
    prev: 'Node' = None
    next: 'Node' = None


@dataclass
class DoublyLinkedList:

    head: Node = None
    tail: Node = None
    size: int = 0

    def addFirst(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addLast(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def add(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if index == 0:
            self.addFirst(value)
        elif index == self.size:
            self.addLast(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    def takeFirst(self):
        if self.head is None:
            raise IndexError("List is empty")
        value = self.head.value
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value

    def takeLast(self):
        if self.tail is None:
            raise IndexError("List is empty")
        value = self.tail.value
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.takeFirst()
        elif index == self.size - 1:
            return self.takeLast()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            value = current.value
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            return value

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def printReversed(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev
