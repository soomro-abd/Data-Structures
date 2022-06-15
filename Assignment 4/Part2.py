class heapNode:
    def __init__(self, value, doc_title=None):
        self.value = value # The integer key of the node
        self.doc_title = doc_title # The node's document title (you'll understand this in Part 3) for a priority queue's implementation in Task 3. Set to None for Task 2
        
class minHeap:
    def __init__(self, cap):
        self.harr = [None] * cap # List of elements in the min-heap
        self.capacity = cap # Maximum possible size of the min-heap
        self.heap_size = 0 # Current number of elements in the min heap (elements of type None don't count)

    # return index of the parent of a node at index i
    def parent (self, i):
        # formula for parent_index = floor[(i-1)/2]
        parent_index = (i-1) // 2
        return parent_index

    # get index of left child of node at index i
    def get_left_child_index (self, i):
        # formula for left child's index = 2i + 1
        left_index = (2*i) + 1
        return left_index

    # get index of right child of node at index i
    def get_right_child_index (self, i):
        # formula for right child's index = 2i + 2
        right_index = (2*i) + 2
        return right_index

    # Returns the minimum node (node at root) from min heap
    def get_min (self):
        return self.harr[0]
    
    # remove minimum node (or root) from min heap
    def extract_min (self):
        
        if self.heap_size == 0:
            return "Error: The heap is empty!"

        root = self.get_min()

        #some useful indices
        last_i = self.heap_size - 1

        #the last element is at heap_size - 1
        last_element = self.harr[last_i]

        #replacing the root with the last element
        self.harr[0] = last_element

        #replacing the last element with None
        self.harr[last_i] = None

        #decreasing the size of the heap
        self.heap_size -= 1

        #fixing the heap structure
        self.percolate_down(0)

        # print (root)
        return root

    # Decreases value of node at index i to new_val (assume new_val will always be smaller than value in harr[i])
    def decrease_node (self, i, new_val):

        #change the value first
        (self.harr[i]).value = new_val

        self.percolate_up(i)

    # Deletes the node stored at index i
    def delete_node (self, i):

        if (i >= self.heap_size):
            return "Error: Index out of range!"
        
        #index of last node
        last_i = self.heap_size - 1

        #last node
        last_node = self.harr[last_i]

        #replacing the node at i with last node
        self.harr[i] = last_node

        #deleting last node
        self.harr[last_i] = None

        #decrementing heap size
        self.heap_size -= 1

        #fixing the heap
        self.percolate_up(i)
        # self.percolate_down(0)

        self.percolate_down(i)

    # Inserts a new node with value 'value'
    def insert_node (self, value, doc_title=None):
        
        new_node = heapNode(value, doc_title)

        if self.heap_size == self.capacity:
            return "Error: The heap is at maximum capacity!"


        #index of insertion
        ii = self.heap_size

        #inserting the node at the next free pos in the array
        self.harr[ii] = new_node

        #increasing the size of heap by 1
        self.heap_size += 1

        #fixing the heap structure
        self.percolate_up(ii)

        
        pass

    # Helper function to percolate_down after editing the heap
    def percolate_down(self, curr_index):
        # percolate down

        if (curr_index < 0):
            return

        #some useful indices
        left_i = self.get_left_child_index(curr_index)
        right_i = self.get_right_child_index(curr_index)


        #getting some useful nodes
        curr_node = self.harr[curr_index]
        left_child = None
        right_child = None

        if left_i < self.capacity:
            left_child = self.harr[left_i]

        if right_i < self.capacity:
            right_child = self.harr[right_i]

        if not curr_node:
            return

        #some usefule values
        curr_val = curr_node.value


        if left_child:
            if right_child:
                #swap with the smallest child if that child is smaller than the node's val
                if left_child.value < right_child.value:
                    #left child is smallest
                    if left_child.value < curr_val:
                        #swap

                        self.harr[curr_index] = left_child
                        self.harr[left_i] = curr_node

                        self.percolate_down(left_i)
                else:
                    #right child is smallest
                    if right_child.value < curr_val:
                        #swap

                        self.harr[curr_index] = right_child
                        self.harr[right_i] = curr_node
                        
                        self.percolate_down(right_i)

            else:
                #left child exists but right doesnt
                if left_child.value < curr_val:
                    #swap

                    self.harr[curr_index] = left_child
                    self.harr[left_i] = curr_node

                    self.percolate_down(left_i)
        else: 
            #no children exist
            return

    # Helper function to percolate_up after editing the heap
    def percolate_up(self, curr_index):

        if curr_index == 0:
            return

        #parent_index
        pi = self.parent(curr_index)

        #parent node
        parent = self.harr[pi]

        #parent_value
        pv = parent.value

        #nodes value
        val = (self.harr[curr_index]).value

        if (pv > val):
            #swap the two nodes and call percolate on parent
            
            temp = self.harr[curr_index]
            self.harr[pi] = temp
            self.harr[curr_index] = parent

            self.percolate_up(pi)

        return

    #Helper function to visualize the heap
    def print_heap(self):

        valArray = [None] * self.capacity

        for i, node in enumerate(self.harr):
            if node:
                valArray[i] = node.value

        print(valArray)





if __name__ == "__main__":
    myMinHeap = minHeap(40)

    heap_values = [34,7,53,12,68,90,24,71,13,3,1,61,18,30,50,11,52,54,56,55,80,97,91,23,29,33,73,77,89,16,20,35,43,47,57,66,88,2,9,64]

    for i in range(40):
        myMinHeap.insert_node(heap_values[i])

    # myMinHeap.insert_node(7)
    # myMinHeap.insert_node(5)
    # myMinHeap.insert_node(4)
    # myMinHeap.insert_node(8)
    # myMinHeap.insert_node(6)
    # myMinHeap.insert_node(19)
    # myMinHeap.insert_node(20)
    # myMinHeap.insert_node(35)

    myMinHeap.print_heap()
    # for i in range(40):
    #     print(myMinHeap.extract_min().value, end = ", ")


    # print(myMinHeap.extract_min().value)
    # myMinHeap.extract_min()

    # myMinHeap.print_heap()
    