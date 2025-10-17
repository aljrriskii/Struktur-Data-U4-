class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # === Hapus sebelum data tertentu ===
    def delete_before(self, value):
        if self.is_empty() or self.head.data == value:
            print("Tidak ada simpul sebelum data tersebut.")
            return
        current = self.head.next
        while current:
            if current.data == value:
                node_to_delete = current.previous
                if node_to_delete.previous:
                    node_to_delete.previous.next = current
                    current.previous = node_to_delete.previous
                else:
                    self.head = current
                    current.previous = None
                print(f"Data sebelum {value} dihapus: {node_to_delete.data}")
                return
            current = current.next
        print("Data tidak ditemukan!")

    # === Hapus setelah data tertentu ===
    def delete_after(self, value):
        if self.is_empty() or self.tail.data == value:
            print("Tidak ada simpul setelah data tersebut.")
            return
        current = self.head
        while current:
            if current.data == value and current.next:
                node_to_delete = current.next
                current.next = node_to_delete.next
                if node_to_delete.next:
                    node_to_delete.next.previous = current
                else:
                    self.tail = current
                print(f"Data setelah {value} dihapus: {node_to_delete.data}")
                return
            current = current.next
        print("Data tidak ditemukan!")

    # === Tambah data di tengah (ubah 0 jadi 2) ===
    def insert_at_middle(self, new_value):
        if self.is_empty():
            print("List masih kosong.")
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(f"Data tengah sebelumnya: {slow.data}")
        slow.data = new_value  # ubah data tengah jadi nilai baru
        print(f"Data tengah diubah menjadi: {new_value}")

    # === Tampilkan dari depan ===
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# =============================
# PROGRAM UTAMA
# =============================

dll = DoubleLinkedList()

# Data awal dari NIM: 240705007
data_nim = [2, 4, 0, 7, 0, 5, 0, 0, 7]
for i in data_nim:
    dll.insert_at_end(i)

print("Data awal:")
dll.display_forward()
print()

# 1️ Hapus data sebelum angka 7
dll.delete_before(2)
dll.display_forward()
print()

# 2️ Hapus data setelah angka 7
dll.delete_after(4)
dll.display_forward()
print()

# 3️ Ubah data tengah (0) jadi 2
dll.insert_at_middle(2)
dll.display_forward()
