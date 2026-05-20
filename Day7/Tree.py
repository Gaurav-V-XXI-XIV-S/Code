#____________________________Tree Data Structure_________________________________#
# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child = []
#         self.parent = None   # ✅ important fix

#     def add_child(self, child):
#         child.parent = self   # ✅ set parent reference
#         self.child.append(child)
#         print(child.data, "Added as child to", self.data)

#     def get_level(self):
#         level = 0
#         p = self
#         while p.parent:
#             p = p.parent
#             level += 1
#         return level

#     def print_tree(self):
#         spaces = " " * self.get_level() * 4
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)

#         for child in self.child:
#             child.print_tree()

#     def __str__(self):
#         return self.data

#     def __repr__(self):
#         return self.data

#     def __iter__(self):
#         return iter(self.child)

#     def __len__(self):
#         return len(self.child)

#     def __getitem__(self, index):
#         return self.child[index]

#     def __setitem__(self, index, value):
#         self.child[index] = value

#     def __delitem__(self, index):
#         del self.child[index]


# # ---------- Testing ----------
# rootnode = Tree("Drinks")

# hot = Tree("Hot")
# cold = Tree("Cold")

# tea = Tree("Tea")
# coffee = Tree("Coffee")

# nonAlcoholic = Tree("Non-Alcoholic")
# alcoholic = Tree("Alcoholic")

# rootnode.add_child(hot)
# rootnode.add_child(cold)

# hot.add_child(tea)
# hot.add_child(coffee)

# cold.add_child(nonAlcoholic)
# cold.add_child(alcoholic)

# rootnode.print_tree() 
#................................................................................#


# class Tree:
#    def __init__(self,data):
#      self.data = data
#      self.child = []

#    def addChild(self, object):
#      self.child.append(object)
#      print("Tree Node Added")

#    def __str__(self, level = 0):
#      ret =" "* level + str(self.data) + "\n"
#      for ch in self.child:
#        ret += ch.__str__(level+1)
#      return ret

# rootNode = Tree("Drinks")
# Hot = Tree("Hot")
# Cold = Tree("Cold")
# Tea = Tree("Tea")
# Coffee= Tree("Coffee")
# NonAlcoholic = Tree("NonAlcoholic")
# Alcoholic= Tree("Alcoholic")

# rootNode.addChild(Hot)  #Left
# rootNode.addChild(Cold)  #Right
# Hot.addChild(Tea)
# Cold.addChild(NonAlcoholic)
# Cold.addChild(Alcoholic)
# print(rootNode)



#____________________________Tree Data Structure Solution__________________________#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     def add_child(self, child):
#         self.children.append(child)

#     def print_tree(self, level=0):
#         print(" " * level * 4 + str(self.data))
#         for child in self.children:
#             child.print_tree(level + 1)

#     # Height of tree = longest path from node to leaf
#     def height(self):
#         if not self.children:
#             return 0

#         return 1 + max(child.height() for child in self.children)


# # ---------------- Example Tree (like your image) ----------------

# root = Node("N1")

# n2 = Node("N2")
# n3 = Node("N3")

# n4 = Node("N4")
# n5 = Node("N5")
# n6 = Node("N6")

# n7 = Node("N7")
# n8 = Node("N8")

# # Build structure
# root.add_child(n2)
# root.add_child(n3)

# n2.add_child(n4)
# n2.add_child(n5)

# n3.add_child(n6)

# n4.add_child(n7)
# n4.add_child(n8)

# # Print tree
# root.print_tree()

# # Height
# print("\nHeight of tree:", root.height())
#................................................................................#

#______________________________Tree Solution___________________________#
# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.child=[]
#     def addChild(self,child):
#         self.child.append(child)
#         print("child added")
#     def __str__(self,level=0):
#         ret="      "*level+str(self.data)+"\n"
#         for ch in self.child:
#             ret+=ch.__str__(level+1)
#         return ret
# a = Tree("N1")
# b = Tree("N2")
# c = Tree("N3")
# d = Tree("N4")
# e = Tree("N5")
# f = Tree("N6")
# g = Tree("N7")
# h = Tree("N8")

# a.addChild(b)
# a.addChild(c)
# b.addChild(d)
# b.addChild(e)
# c.addChild(f)
# d.addChild(g)
# d.addChild(h)
# print(a)
#................................................................................#

#_____________Time Complexity of Linked List and Tree________________________#
# Linked List: O(n) for search, O(1) for insertion/deletion at head, O(n) for insertion/deletion at tail
# Tree: O(n) for search in general, O(log n) for balanced trees,
# O(1) for insertion/deletion at root, O(n) for insertion/deletion at leafs
# Note: Complexity can vary based on tree type (e.g., binary search tree, AVL tree, etc.)
#................................................................................#


def rotate_array(arr, k):
    k = k % len(arr) 
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(arr, k))  # Output: [4, 5, 1, 2, 3]