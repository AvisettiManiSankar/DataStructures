# Chaining Method ==>
# class HashTable:
#     def __init__(self):
#         self.size = 10
#         self.arr = [[] for _ in range(self.size)]

#     def get_hashvalue(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash%self.size
    
#     def __setitem__(self, key, value):
#         index = self.get_hashvalue(key)
#         found = False
#         for idx, item in enumerate(self.arr[index]):
#             if item[0] == key:
#                 self.arr[index][idx] = (key, value)
#                 found = True
#         if not found:
#             self.arr[index].append((key,value))

#     def __getitem__(self, key):
#         index = self.get_hashvalue(key)
#         for item in self.arr[index]:
#             if item[0] == key and len(item) == 2:
#                 return item[1]
#             else:
#                 return None
    
#     def __delitem__(self, key):
#         index = self.get_hashvalue(key)
#         for idx, item in enumerate(self.arr[index]):
#             if item[0] == key:
#                 del self.arr[index][idx]
    
# hash_var = HashTable()

# hash_var['name']='mani'
# hash_var['name']='nani'

# print(hash_var['name'])
# del hash_var['name']
# print(hash_var.arr)

# Linear Probing ==>
class HashTable:
    def __init__(self):
        self.size = 10
        self.arr = [None for _ in range(self.size)]

    def get_hashvalue(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash%self.size
    
    def __setitem__(self, key, value):
        index = self.get_hashvalue(key)
        found = False
        for i in [*range(index,self.size)]+[*range(0,index)]:
            if self.arr[i] is None:
                self.arr[i] = (key,value)
                found = True
                break
            elif self.arr[i][0] == key:
                self.arr[i] = (key,value)
                return None
        if not found:
            raise Exception('HashMap Full')

    def __getitem__(self, key):
        index = self.get_hashvalue(key)
        for i in [*range(index,self.size)] + [*range(0,index)]:
            if self.arr[i] is None:
                return None
            elif self.arr[i][0] == key:
                return self.arr[i][1]
        return None
    
    def __delitem__(self, key):
        index = self.get_hashvalue(key)
        for i in [*range(index,self.size)] + [*range(0,index)]:
            if self.arr[i] is None:
                return None
            elif self.arr[i][0] == key:
                self.arr[i] = None
    
hash_var = HashTable()

hash_var['name_bc']='mani'
hash_var['name_bc']='mani1'
print(hash_var.arr)
print(hash_var['name_bc'])
del hash_var['name_bc']
print(hash_var.arr)