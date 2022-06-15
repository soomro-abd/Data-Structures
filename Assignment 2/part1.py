# Assignment 2-Part 1
# BST

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):

    def __init__(self): # Initializing the BST. Root points to None.
        self.root = None

    #time-complexity = O(n)
    def print_tree_helper(self, root):
        """
        prints a tree inorder 
        Made this for testing purposes
        """

        if root != None:
            self.print_tree_helper(root.left)
            print(root.value, end = "\t")
            self.print_tree_helper(root.right)

    #time-complexity = O(n)
    def print_tree(self):
        self.print_tree_helper(self.root)
        print(" ")

    #time-complexity = O(n)
    def in_order_helper(self, root):
        result = list()

        if root != None:
            result += self.in_order_helper(root.left)
            result.append(root.value)
            result += self.in_order_helper(root.right)

        return result

    #time-complexity = O(n)
    def in_order(self):
           return self.in_order_helper(self.root)
        

    #time-complexity = O(n)
    def pre_order_helper(self, root):

        result = list()

        if root != None:
            result.append(root.value)
            result += self.pre_order_helper(root.left)
            result += self.pre_order_helper(root.right)
    
        return result

    #time-complexity = O(n)
    def pre_order(self):
        return self.pre_order_helper(self.root)


    #time-complexity = O(n)
    def post_order_helper(self, root):

        result = list()

        if root != None:
            result += self.post_order_helper(root.left)
            result += self.post_order_helper(root.right)
            result.append(root.value)   
        
        return result

    #time-complexity = O(n)
    def post_order(self):
        return self.post_order_helper(self.root)


    #time-complexity = O(n)
    def insert_helper(self, root, val):

        if root == None:
            return Node(val)
        
        if root.value == val:
            return False
        elif val > root.value:
            root.right = self.insert_helper(root.right, val)
        else:
            root.left = self.insert_helper(root.left, val)

        return root

    #time-complexity = O(n)
    def insert(self, val):
        self.root =  self.insert_helper(self.root, val)

    
    #time-complexity = O(n)
    def get_node_helper(self, root, key):

        if (root != None):
            if (root.value == key):
                return root
            elif key > root.value:
                return (self.get_node_helper(root.right, key))
            else:
                return (self.get_node_helper(root.left, key))
        else:
            return False

    #time-complexity = O(n)
    def get_node(self, key):

        return self.get_node_helper(self.root, key)

    #time-complexity = O(n)        
    def find_node(self, key):
        return bool(self.get_node(key))

    #time-complexity = O(n)        
    def get_children(self, key):
        return [self.get_node(key).left, self.get_node(key).right]
    
    #time-complexity = O(n)
    def update_node(self, key, val):
        
        if self.get_node(key):
            self.get_node(key).value = val
        else:
            return False
    
    #time-complexity = O(n)    
    def get_height_helper(self, root):

        if root == None:
            return 0
        else:
            return (max(self.get_height_helper(root.left), self.get_height_helper(root.right)) + 1)


    #time-complexity = O(n)
    def get_height(self):
        
        return self.get_height_helper(self.root)
        
    #time-complexity = O(n)
    def get_path_helper(self, root, key):

        path = list()

        if root != None:
            path.append(root.value)

            if root.value == key:
                return path
            elif root.value < key:
                path += self.get_path_helper(root.right, key)
            else:
                path += self.get_path_helper(root.left, key)
            pass
        else:
            return False

        return path

    #time-complexity = O(n)
    def get_path(self, key):
        return self.get_path_helper(self.root, key)
        

    #time-complexity = O(n)
    def averager(self, root):
        
        return (sum(self.in_order_helper(root)) / len(self.in_order_helper(root)))

    #time-complexity = O(n)
    def avg_diff(self):

        return (self.averager(self.root.right) - self.averager(self.root.left)) 


    #time-complexity = O(n)
    def get_left_most(self, root, key):

        while root.left != None:
            return self.get_left_most(root.left, key)
        
        return root

    #time-complexity = O(n)
    def get_right_most(self, root, key):

        while root.right != None:
            return self.get_right_most(root.right, key)

        return root

    #time-complexity = O(n)
    def delete_helper(self, root, key):
        """
        If no child, then delete.
        If only one child, make its extreme opposite the root. 
        If two child, follow inorder. 

        When val is replaced, then delete the replacer. 
        """

        if root != None:
            if root.value == key:
                if not(root.left or root.right):
                    #no children
                    return None
                elif root.left == None:
                    return root.right
                elif root.right == None:
                    return root.left
                else:
                    new_val = self.get_left_most(root.right).value
                    root.value = new_val
                    root.right = self.delete_helper(root.right, new_val)
            elif key > root.value:
                root.right = self.delete_helper(root.right, key)
            elif key < root.value:
                root.left = self.delete_helper(root.left, key)
        else:
            return None

        return root


    #time-complexity = O(n)
    def delete(self, key):
        self.root = self.delete_helper(self.root, key)

    #time-complexity = O(n)
    def delete_leaf(self, key):
        
        temp_node = self.get_node(key)
        if not(temp_node.left or temp_node.right):
            self.delete(key)
        else:
            return False

    #time-complexity = O(1)
    def is_leaf(self, node):
        return not(node.left or node.right)

    #time-complexity = O(n)
    def delete_leaves_helper(self, root):
        
        if root != None:
            if self.is_leaf(root):
                root = self.delete(root.value)
                return root
            root.left = self.delete_leaves_helper(root.left)
            root.right = self.delete_leaves_helper(root.right)
        else:
            return None

        return root
    
    #time-complexity = O(n)
    def delete_leaves(self):
        self.root = self.delete_leaves_helper(self.root)
        

# Testing Area ---

# You can create a class tree object below and check the implementation of your functions.
# Make sure to comment out the code before running the tests else it might mix up the results.
def main():
    # Create an object here to test the functions.
    # test_BST = Tree()
    # test_BST.root = Node(10)
    # test_BST.root.left = Node(5)
    # test_BST.root.right = Node(20)
    
    test_BST = Tree()
    test_BST.insert(16)
    test_BST.root = Node(6)
    test_BST.root.left = Node(5)
    test_BST.root.right = Node(7)
    test_BST.root.left.left = Node(4)
    test_BST.root.left.right = Node(5.5)
    test_BST.root.right.left = Node(6.5)
    test_BST.root.right.right = Node(8)

    # test_BST.insert(5)
    # test_BST.insert(20)
    # test_BST.insert(7)
    # test_BST.insert(100)

    print(test_BST.in_order())


    test_BST.delete_leaves()

    # print(test_BST.get_path_helper(test_BST.root, 5))
    print(test_BST.in_order())
    # Write code here


# Comment out the line below before running your test files.
main()
