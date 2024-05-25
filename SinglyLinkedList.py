class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                raise IndexError
            current = current.next
        current.next = current.next.next

    def return_size(self):
        count, current = 0, self.head
        while current:
            count += 1
            current = current.next
        return count

    def empty(self):
        return self.head is None

    def rotate(self, k):
        if not self.head or k <= 0:
            return
        length = self.return_size()
        k %= length
        if k == 0:
            return
        fast, slow = self.head, self.head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        new_head = slow.next
        slow.next = None
        fast.next = self.head
        self.head = new_head

    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = other_list.head

    def interleave(self, other_list):
        temp = Node(None)
        tail = temp
        curr1, curr2 = self.head, other_list.head

        while curr1 or curr2:
            if curr1:
                tail.next = curr1
                tail = tail.next
                curr1 = curr1.next
            if curr2:
                tail.next = curr2
                tail = tail.next
                curr2 = curr2.next

        self.head = temp.next

    def middle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def index_of(self, value):
        current, index = self.head, 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def split_at_index(self, index):
        if index < 0:
            raise IndexError
        new_list = SinglyLinkedList()
        if index == 0:
            new_list.head = self.head
            self.head = None
            return new_list
        current = self.head
        for _ in range(index - 1):
            if not current:
                raise IndexError
            current = current.next
        new_list.head = current.next
        current.next = None
        return new_list




