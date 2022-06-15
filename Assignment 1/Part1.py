# Assignment 1-Part 1
# Linked Lists

# Single Node Class
from cgi import test


class Node:
    def __init__(self, data):
        self.data = data  # Assign data to node
        self.next = None  # Node initially does not point to any other node
  
# Linked List class
class LinkedList:
    # Initializing the linked list object. Head points to None.
    def __init__(self):
        self.head = None

    # Already provided
    def print_list(self):
        traverse = self.head
        LinkedList = []
        while(traverse):
            LinkedList.append(traverse.data)
            traverse = traverse.next
        return LinkedList

    #helper-function-1 : returns the tail node
    def get_tail_node(self):
        if not self.head:
            return None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            
            return temp

    #helper-function-2: returns any Node at position n if it exists, None otherwise
    def get_node(self, pos):
        
        length = self.get_length()

        if (pos >= length) or (pos < 0):
            return None
        else:
            temp_node = self.head
            for i in range(pos):
                temp_node = temp_node.next
            
            return temp_node

            
        
    
    # To-do Function 1
    #time-complexity = O(1)
    def get_head(self):
        if not(self.head):
            return None
        else:
            return (self.head).data
    
    # To-do Function 2
    #time-complexity = O(n)
    def get_tail(self):
        tail_node = self.get_tail_node()

        if tail_node:
            return tail_node.data
        else:
            return None
        
    # To-do Function 3
    #time-complexity = O(1)
    def is_empty(self):
        if self.head:

            #list is not empty
            return False

        else: 
            return True
    
    # To-do Function 4
    #time-complexity = O(1)
    def insert_at_head(self, data):

        #creates a new node
        new_node = Node(data)

        #new node now points to where head was pointing
        (new_node).next = self.head

        #now head point to new node
        self.head = new_node

    # To-do Function 5
    #time-complexity = O(n) 
    def insert_at_tail(self, data):

        #creates a new node
        new_node = Node(data)

        tail_node = self.get_tail_node()

        if tail_node:
            tail_node.next = new_node
        else: 
            self.head = new_node


    # To-do Function 6
    # Assume both the node to be inserted after and before exist in the right order in the test set
    #time-complexity = O(n)
    def insert_in_between(self, data, after, before):
        
        new_node = Node(data)

        temp_node = self.head

        while temp_node.data != after:
            temp_node = temp_node.next
        
        new_node.next = temp_node.next
        temp_node.next = new_node

        pass
    
    # To-do Function 7   
    # time-complexity = O(1) 
    def delete_head(self):
        if self.head:

            #making sure the second node exists
            if (self.head).next:

                #make a new node, have it point to the second node (the node that head was pointing to)
                new_node = (self.head).next

                #head points to the new node
                self.head = new_node

                #lucky me, python takes care of garbage collection
            else:
                self.head = None
        else:
            return None

             
    # To-do Function 8
    # time-complexity = O(n)
    def delete_tail(self):
        if self.is_empty():
            return None
        else:
            before_tail = self.head

            #if the list has one element, delete the only node
            if not before_tail.next:
                self.head = None

            else:
                while (before_tail.next).next:
                    before_tail = before_tail.next

                #after this loop the var before_tail stores the second last node
                before_tail.next = None

    # To-do Function 9
    #time-complexity = O(n)
    def delete_any(self, data):
        
        if self.get_head() == data:
            self.delete_head()

        elif self.get_tail() == data:
            self.delete_tail()

        else:
            node_to_be_deleted = self.head.next
            node_before = self.head

            while node_to_be_deleted.data != data and node_to_be_deleted:
                node_to_be_deleted = node_to_be_deleted.next
                node_before = node_before.next

            # *poof*
            node_before.next = node_to_be_deleted.next

    # To-do Function 10
    #time-complexity = O(n)
    def get_length(self):

        #for ease
        head = self.head
        length = 1

        if not head:
            return 0
        elif not head.next:
            return 1
        else:
            while (head.next):
                length += 1
                head = head.next

            return length
    
    # To-do Function 11
    #time-complexity = O(n)
    def get_element(self, data):
        if not self.head:
            return False
        else: 
            temp_node = self.head
            temp_data = temp_node.data

            while temp_node:
                if temp_data == data:
                    return data
                else:
                    temp_node = temp_node.next
                    
                    if not temp_node:
                        return False

                    temp_data = temp_node.data

    
    # To-do Function 12
    #time-complexity = O(n)
    def reverse_list(self):
        if self.is_empty():
            return None
        elif self.get_length() == 1:
            pass
        elif self.get_length() == 2:

            head = self.head
            next_node = head.next
            
            next_node.next = head
            head.next = None
            
            self.head = next_node
            
        else:
            head = self.head

            #storing the first three nodes in temp vars
            temp_var_1 = head
            temp_var_2 = temp_var_1.next
            temp_var_3 = temp_var_2.next

            head.next = None

            
            while temp_var_3:
                temp_var_2.next = temp_var_1

                temp_var_1 = temp_var_2
                temp_var_2 = temp_var_3
                temp_var_3 = temp_var_3.next

            temp_var_2.next = temp_var_1
            self.head = temp_var_2





# Testing Area ---

# You can create a class Linked List object below and check the implementation of your functions.
# Make sure to comment out the code before running the tests else it might mix up the results.
# def main():
#     # Create an object here to test the functions.
#     test_list = LinkedList()
#     # Write code here
#     test_list.insert_at_head('a')
#     test_list.insert_at_head('b')
#     test_list.insert_at_head('c')
#     test_list.insert_at_tail('d')
    
#     print(test_list.get_head(), '\n')
#     #print(test_list.head, '\n')
#     print(test_list.get_tail(), '\n')
#     print(test_list.is_empty(), '\n')
    

#     print(test_list.print_list(), test_list.get_length(), '\n')
#     print(test_list.get_node(0).data, '\n')
#     print(test_list.get_node(1).data, '\n')
#     print(test_list.get_node(2).data, '\n')
#     print(test_list.get_node(3).data, '\n')

#     test_list.insert_in_between('r', 'a', 'd')
#     print(test_list.print_list(), test_list.get_length(), '\n')

#     test_list.delete_any('c')
#     print(test_list.print_list(), test_list.get_length(), '\n')
#     test_list.reverse_list()
#     print(test_list.print_list(), test_list.get_length(), '\n')
    
    
    
    
# # Comment out the line below before running your test files.
# main()