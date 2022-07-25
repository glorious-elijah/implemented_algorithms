'''A python implementation of a binary tree data structure'''
import random

class Node:
    '''Represents a node in a tree'''
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self) -> str:
        return f'{self.data} L-{self.left} R-{self.right}'

    def type_of(self) -> int:
        '''Return type of data stored in node'''
        return type(self.data)


class BinaryTree:
    '''Represents a binary tree data structure'''
    def __init__(self) -> None:
        self.root = None

    def __repr__(self) -> str:
        return f'Root {self.root}'

    def insert(self,data):
        '''Inserts data into the closest available node'''
        current = self.root
        direction = ['left','right']

        if current is self.root and not current:
            self.root = Node(data)
            return

        while current:
            if not current.left:
                current.left = Node(data)
                return

            if not current.right:
                current.right = Node(data)
                return

            index = random.randint(1, 2) % 2

            if direction[index] == 'left':
                current = current.left
            else:
                current = current.right

    def replace_root_left(self, data):
        '''Insert a new node to the root and move old node to the left leaf '''
        # replaces the root with a new node and
        # pushes the old root to the left node or the right node

        temp = self.root
        self.root = Node(data)
        self.root.left = temp

    def replace_root_right(self, data):
        '''Insert a new node to the root and move old node to the right leaf '''
        # replaces the root with a new node and
        # pushes the old root to the right node or the right node

        temp = self.root
        self.root = Node(data)
        self.root.right = temp

    def insert_left(self, data):
        '''Insert Data to the leftmost available node'''
        current = self.root

        while current:
            if not current.left:
                break
            current = current.left

        new_node = Node(data)
        current.left = new_node

    def insert_right(self,data):
        '''Insert data to the rightmost available node'''
        current = self.root

        while current:
            if not current.right:
                break
            current = current.right

        new_node = Node(data)
        current.right = new_node

    # def inorder(self): # TODO - Go through code //inorder traversal without recurssion or stack//
    #     '''Returns a list of data stored in the tree when traversed inorder'''
    #     current = self.root

    #     while current:
    #         if not current.left:
    #             print(current.data)
    #             current = current.right
    #         else:
    #             pre = current.left
    #             while pre.right and pre.right is not current:
    #                 pre = pre.right
    #             if not pre.right:
    #                 pre.right = current
    #                 current = current.left
    #             else:
    #                 pre.right = None
    #                 print(current.data)
    #                 current = current.right

    def inorder(self, root, stack = []): #inorder with recurssion
        '''Inorder traversal of a tree'''
        if root:
            self.inorder(root.left, stack)
            stack.append(root.data)
            self.inorder(root.right, stack)
        return stack

    def preorder(self,root, stack = []):
        '''Preorder traversal of a tree'''
        if root:
            stack.append(root.data)
            self.preorder(root.left,stack)
            self.preorder(root.right, stack)
        return stack

    def postorder(self,root, stack = []):
        '''Postorder traversal of a tree'''
        if root:
            self.postorder(root.left, stack)
            self.postorder(root.right, stack)
            stack.append(root.data)
        return stack

    def search(self,key):
        '''Search for the existence of key in tree'''
        current = self.root

        for data in self.inorder(current):
            if key == data:
                return True

        return False


c = BinaryTree()
c.insert(1)
c.insert(2)
c.insert(3)
c.insert(4)
c.insert(5)
c.insert(6)
c.insert(7)
print(c.search(7))
# d = c.inorder(c.root)
# print(d)
