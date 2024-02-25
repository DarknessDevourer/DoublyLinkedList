import unittest
import Dataclass


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = Dataclass.DoublyLinkedList()

    def test_addFirst(self):
        self.dll.addFirst(1)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(self.dll.size, 1)

    def test_addLast(self):
        self.dll.addLast(1)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(self.dll.size, 1)

    def test_add(self):
        self.dll.add(0, 1)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(self.dll.size, 1)

        self.dll.add(1, 2)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.head.next.value, 2)
        self.assertEqual(self.dll.tail.value, 2)
        self.assertEqual(self.dll.size, 2)

    def test_takeFirst(self):
        self.dll.addLast(1)
        self.dll.addLast(2)
        self.assertEqual(self.dll.takeFirst(), 1)
        self.assertEqual(self.dll.head.value, 2)
        self.assertEqual(self.dll.tail.value, 2)
        self.assertEqual(self.dll.size, 1)

    def test_takeLast(self):
        self.dll.addLast(1)
        self.dll.addLast(2)
        self.assertEqual(self.dll.takeLast(), 2)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(self.dll.size, 1)

    def test_remove(self):
        self.dll.addLast(1)
        self.dll.addLast(2)
        self.dll.addLast(3)
        self.assertEqual(self.dll.remove(1), 2)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.head.next.value, 3)
        self.assertEqual(self.dll.tail.value, 3)
        self.assertEqual(self.dll.size, 2)

    def test_set(self):
        self.dll.addLast(1)
        self.dll.addLast(2)
        self.dll.set(1, 3)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.head.next.value, 3)
        self.assertEqual(self.dll.tail.value, 3)
        self.assertEqual(self.dll.size, 2)

    def test_get(self):
        self.dll.addLast(1)
        self.dll.addLast(2)
        self.assertEqual(self.dll.get(1), 2)

    def test_printReversed(self):
        import sys
        from io import StringIO

        self.dll.addLast(1)
        self.dll.addLast(2)

        captured_output = StringIO()
        sys.stdout = captured_output

        self.dll.printReversed()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "2\n1\n")


if __name__ == '__main__':
    unittest.main()
