import Dataclass

dll = Dataclass.DoublyLinkedList()
dll.addLast(1)
dll.addLast(2)
dll.addLast(3)
dll.addLast(4)

assert dll.takeLast() == 4
assert dll.takeLast() == 3
assert dll.size == 2


print("Список після перевірки 1:", end=' ')
current = dll.head
while current:
    print(current.value, end=' ')
    current = current.next
print()


dll = Dataclass.DoublyLinkedList()
dll.addFirst(1)
dll.addFirst(2)
dll.addFirst(3)
dll.addFirst(4)

assert dll.takeFirst() == 4
assert dll.takeFirst() == 3
assert dll.size == 2


print("Список після перевірки 2:", end=' ')
current = dll.head
while current:
    print(current.value, end=' ')
    current = current.next
print()
