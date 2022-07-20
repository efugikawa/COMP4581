# Hash Table ADT with chaining implementation
# Elizabeth Fugikawa, summer 2022

# These hash tables accept only strings and hashes based on their ASCII value of the first char
# given implementation that uses chaining
class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.table = []
        for i in range(self.size):
            self.table.append([])

    def __str__(self):
        return str(self.table)

    def insert(self, elem):
        hash = ord(elem[0]) % self.size
        self.table[hash].append(elem)

    def member(self, elem):
        hash = ord(elem[0]) % self.size
        return elem in self.table[hash]

    def delete(self, elem):
        hash = ord(elem[0]) % self.size
        self.table[hash].remove(elem)


# created implementation that uses open addressing (linear probing)
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for i in range(size)]
        self.status = ["Empty" for i in range(size)]

    def __str__(self):
        return str(self.table)

    def insert(self, elem):
        i = 0
        while i < self.size:
            hash = (ord(elem[0]) + i) % self.size
            if self.table[hash] is None and self.status[hash] != "Filled":
                self.table[hash] = elem
                self.status[hash] = "Filled"
                print("Inserted", elem)
                return
            else:
                i += 1

    def member(self, elem):
        i = 0
        while i < self.size:
            hash = (ord(elem[0]) + i) % self.size
            if self.table[hash] is None and self.status[hash] == "Empty":
                return False
            elif self.table[hash] == elem:
                return True
            i += 1
        return False

    def delete(self, elem):
        i = 0
        while i < self.size:
            hash = (ord(elem[0]) + i) % self.size
            if self.table[hash] == elem:
                self.table[hash] = None
                self.status[hash] = "Deleted"
                print("Deleted", elem)
                return
            i += 1


# Testing code
# s = MyHashTable(10)  # via chaining
s = HashTable(10)  # via linear probing / open addressing
s.insert("amy")  # 97
s.insert("chase")  # 99
s.insert("chris")  # 99
print("amy is member", s.member("amy"))
print("chris is member", s.member("chris"))
print("alyssa is member", s.member("alyssa"))
s.delete("chase")
print("chris is member", s.member("chris"))
print(s)
