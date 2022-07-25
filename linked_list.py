'''
An implementation of a singly linked data structure
'''

class Node:
    '''
        An object for storing a single node in a singly linked list module
        Contains two attributes the data being stored at the node and a reference to the next node
    '''
    def __init__(self,data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f'<Node {self.data}>'

    def typeof(self):
        '''
        Returns type of data being stored
        '''
        return type(self.data)


class LinkedList:
    '''
        A singly linked list
    '''

    def __init__(self):
        self.head = None

    def __repr__(self):
        node = []
        current = self.head
        while current:
            if current is self.head:
                node.append(f'Head: {current.data}')
            # elif current is self.tail:
            #     node.append('Tail: %s' % current.data)
            elif current.next_node is None:
                node.append(f'Tail: {current.data}')
            else:
                node.append(f'{current.data}')
            current = current.next_node
        return '-> '.join(node)

    def is_empty(self):
        '''
            Returns True if list is empty and vice versa
        '''
        return self.head is None

    def size_of(self):
        '''
        Returns length of list
        '''
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def contains(self, key):
        '''
        A contains method that evaluates to True
        if the key is found in the list and False if otherwise
        '''

        current = self.head

        while current:
            if current.data == key:
                return True
            current = current.next_node
        return False

    def at_index(self, index):
        '''
        Returns the node at an index
        '''
        current = self.head
        i = 0

        if index >= self.size_of():
            return 'Invalid Index'
        while current:
            if i == index:
                return current
            i += 1
            current = current.next_node

    def slice(self, start = 0, stop = -1):
        '''
        Returns a new linked list with the sliced nodes
        Slice returns n-1 nodes in the range given
        '''
        new_list = LinkedList()
        new_list.append(self.at_index(start).data)
        new_start = start + 1

        if start < 0 or stop > self.size_of():
            return 'Invalid Index'

        if stop == -1:
            new_stop = self.size_of() - 1
            while new_start <= new_stop:
                new_list.append(self.at_index(new_start).data)
                new_start += 1
        else:
            new_stop = stop - 1
            while new_start <= new_stop:
                new_list.append(self.at_index(new_start).data)
                new_start += 1

        return new_list


    #end utility-functions

    def insert(self, data, index = 0):
        '''
            Function takes two arguments, data and index, index describes the positional node
            to be replaced with the data passed to the argument.
            Omitting the index argument will assign the index
            a value of 0 to replace the first element or head of the list.
        '''
        try:
            if index == 0:
                return self.prepend(data)

            current = self.head

            while index > 1:
                current = current.next_node
                index -= 1

            new_node = Node(data)
            new_node.next_node = current.next_node
            current.next_node = new_node

            return new_node

        except IndexError:
            return 'Invalid Index'

    def prepend(self, data):
        '''
            Insert data to the head of the linked list
        '''

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

        return new_node

    def append(self, data):
        '''
            Insert data to the tail of the linked list
        '''
        self.insert(data, self.size_of())

    def remove_at_index(self, index = 0):
        '''
            Function take an index argument, index describes the positional node to be removed.
            Omitting the index argument will assign the index a
            value of 0 to remove the first element or head of the list.
        '''
        current = self.head
        try:
            if index == 0:
                #when index is 0 assigns the head to the head.next_node
                #(which contains the next node from the head of the list)
                self.head = current.next_node
                return current

            #assigns the head to the current which keeps track of our node at n
            # Previous tracks the n-1 node
            previous = None

            while index > 0:
                # iterates through the nodes to find the node in the
                # position just before the position we would like to remove
                # when current node is not equal to 0 or the target
                # index then set previous to the current node at n
                # and assign current.next_node( our node at n + 1)
                # to current(which is our node at n)

                previous = current
                current = current.next_node

                #reduces the index by 1
                index -= 1

            # this block of code sets previous (n-1) node's next_node
            # reference to node at n+1 instead of node at n
            previous.next_node = current.next_node
            return current

        except IndexError:
            return 'Invalid Index'

    def remove(self, key):
        '''
            Function takes a key argument, and removes this
            key if found in the list and returns the removed
            node or Invalid Key if not found in list.
        '''

        current = self.head
        # when data being removed is data stored in the head node

        if current.data == key and current is self.head:
            self.head = current.next_node
            return current

        # assigns the head to the current which keeps track of our node at n
        # Previous tracks the n-1 node

        current = self.head
        previous = None

        try:
            while current.data != key:
                # iterates through the nodes to find the node in the position
                # just before the position we would like to remove
                # when current node data is not same as the key then
                # set previous to the current node at n
                # and assign current.next_node( our node at n + 1) to
                # current(which is our node at n)
                previous = current
                current = current.next_node

            # this block of code sets previous (n-1) node's
            # next_node reference to node at n+1 instead of node at n
            previous.next_node = current.next_node
            return current

        except ValueError:
            return 'Invalid Key'


    def remove_all(self, key):
        '''
            Function takes a key argument, and removes all occurrences of
            key if in the list and returns the removed node with a count
            or Invalid Key if not found in list.
        '''

        size = self.size_of()

        while size >= 0:
            self.remove(key)
            size -= 1
