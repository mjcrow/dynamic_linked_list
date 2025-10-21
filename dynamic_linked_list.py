import random

class ListNode:
    def __init__(self, val = "", next = None):
        self.val = val
        self.next = next

class PlayList:
    
    def __init__(self):
        self.head = ListNode("HEAD")
        self.tail = self.head

    def get(self, index: int) -> str:
        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return "Not found"

    def insertHead(self, val: str) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: str) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        while i < index and current:
            i += 1
            current = current.next
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def listSongs(self) -> list[str]:
        current = self.head.next
        res = []
        while current:
            res.append(current.val)
            current = current.next
        return res

    def find(self, title: str) -> int:
        current = self.head.next
        index = 0
        while current:
            if current.val == title:
                return index
            current = current.next
            index += 1
        return -1
    
    def reverse(self) -> None:
        prev = None
        current = self.head.next
        self.tail = current

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head.next = prev

    
def shuffle(self) -> None:

    current = self.head.next
    songs = []
    while current:
        songs.append(current.val)
        current = current.next

    random.shuffle(songs)

    self.head.next = None
    self.tail = self.head
    for song in songs:
        self.insertTail(song)




    

"""
    prev = None
current = head
while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
head = prev
"""

    