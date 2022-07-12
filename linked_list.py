class node:
    '''
        An object for storing a single node in a singly linked list module
        Contains two attributes the data being stored at the node and a reference to the next node
    '''
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data
    
    def __repr__(self):
        return '<Node %s>' %self.data


class linked_list:
    '''
        A singly lined list
    '''

    def __init__(self):
        self.head = None
        # self.tail = None

    
    def __repr__(self):
        node = []
        current = self.head

        while current:
            if current is self.head:
                node.append('Head: %s' % current.data) 
            # elif current is self.tail:
            #     node.append('Tail: %s' % current.data)
            elif current.next_node is None:
                node.append('Tail: %s' % current.data)
            else:
                node.append('%s' % current.data)
            
            current = current.next_node
        return '-> '.join(node)

    def is_empty(self):
        return self.head == None

    def size_of(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count
    
    def prepend(self, data):
        '''
            Insert data to the head of the linked list
        '''

        new_node = node(data)
        new_node.next_node = self.head
        self.head = new_node

    def append(self, data):
        '''
            Insert data to the tail of the linked list
        '''
        self.insert(data, self.size_of())

    def contains(self, key):
        '''
            A contains method that evaluates to True if the key is found in the list and False if otherwise
        '''

        current = self.head

        while current:
            if current.data == key:
                return True
            else:
                current = current.next_node
        return False


    def insert(self, data, index = 0):
        '''
            Function takes two arguments, data and index, index describes the positional node to be replaced with the data passed to the argument. Omitting the index argument will assign the index a value of 0 to replace the first element or head of the list.
        '''
        try:
            if index == 0:
                #when index is 0 calls the prepend function
                self.prepend(data)
            else:
                #assigns the head to the current variable 
                current = self.head


                while index > 1:
                # iterates through the nodes to find the node in the position just before the position we would like to insert
                    current = current.next_node
                    #reduces the index by 1
                    index -= 1
                
                #creates a new node with data(argument from insert function) called new_node
                new_node = node(data)
                #temporary storage of the next_node from our current node
                temp_node = current.next_node
                #assigns the temporary node to the next node of our new_node
                new_node.next_node = temp_node
                #assigns our new_node to the next_node of our current(which is at position n-1 from our target node for replacement)
                current.next_node = new_node
        except:
            return 'Invalid Index'

    def remove_at_index(self, index = 0):
        '''
            Function take an index argument, index describes the positional node to be removed. Omitting the index argument will assign the index a value of 0 to remove the first element or head of the list.
        '''
        current = self.head
        try:
            if index == 0:
                #when index is 0 assigns the head to the head.next_node(which contains the next node from the head of the list)
                self.head = current.next_node
                return current
            else:
                #assigns the head to the current which keeps track of our node at n
                # Previous tracks the n-1 node  
                previous = None

                while index > 0:
                    # iterates through the nodes to find the node in the position just before the position we would like to remove
                    #when current node is not equal to 0 or the target index then set previous to the current node at n
                    #and assign current.next_node( our node at n + 1) to current(which is our node at n)

                    previous = current
                    current = current.next_node

                    #reduces the index by 1
                    index -= 1

                #this block of code sets previous (n-1) node's next_node reference to node at n+1 instead of node at n
                previous.next_node = current.next_node
                return current
        except:
            return 'Invalid Index'

    def remove(self, key):
        '''
            Function takes a key argument, and removes this key if found in the list and returns the removed node or Invalid Key if not found in list.
        '''
        
        current = self.head
        #when data being removed is data stored in the head node
        if current.data == key and current is self.head:
            self.head = current.next_node
            return current

        else:
            #assigns the head to the current which keeps track of our node at n
            # Previous tracks the n-1 node  
            current = self.head
            previous = None

            try:
                while current.data != key:
                    # iterates through the nodes to find the node in the position just before the position we would like to remove
                    #when current node data is not same as the key then set previous to the current node at n
                    #and assign current.next_node( our node at n + 1) to current(which is our node at n)
                    previous = current
                    current = current.next_node

                #this block of code sets previous (n-1) node's next_node reference to node at n+1 instead of node at n
                previous.next_node = current.next_node
                return current

            except:
                return 'Invalid Key'  


    def remove_all(self, key):
        '''
            Function takes a key argument, and removes all occurrences of key if in the list and returns the removed node with a count or Invalid Key if not found in list.
        '''
    
        size = self.size_of()
    
        while size >= 0:
            self.remove(key)
            size -= 1                