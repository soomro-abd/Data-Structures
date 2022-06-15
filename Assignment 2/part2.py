# Assignment 2-Part 2
# AVL Trees




class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.h = 1



class AVLTree(object):


    #time-complexity = O(n)
    def balancer(self, root):
        
        if root != None:
            root.l = self.balancer(root.l)
            root.r = self.balancer(root.r)
        
            if self.get_bal(root) > 1:
                if self.get_bal(root.l) >= 0:
                    #LL rotation
                    root = self.r_rotate(root)
                else:
                    #LR rotation
                    root.l = self.l_rotate(root.l)
                    root = self.r_rotate(root)
            elif self.get_bal(root) < -1:
                if self.get_bal(root.r) <= 0:
                    #RR rotation
                    root = self.l_rotate(root)
                else:
                    #RL rotation
                    root.r = self.r_rotate(root.r)
                    root = self.l_rotate(root)
            else:
                return root
        else:
            return None

        return root


    #time-complexity = O(log n)
    def insert(self, root, key):
        if root == None:
            return TreeNode(key)
        
        if root.value == key:
            return False
        elif key > root.value:
            root.r = self.insert(root.r, key)
        else:
            root.l = self.insert(root.l, key)

        # balancing
        root = self.balancer(root)

        return root
    

    #time-complexity = O(1)
    def l_rotate(self, z):


        if z is None:
            return

        right_child = z.r
        rights_left = right_child.l

        right_child.l = z
        z.r = rights_left

        return right_child


    #time-complexity = O(1)
    def r_rotate(self, z):
        
        if z is None:
            return

        
        left_child = z.l
        lefts_right = left_child.r


        left_child.r = z
        z.l = lefts_right

        return left_child


    #time-complexity = O(n)
    def get_height(self,root):
        if root == None:
            return 0
        else:
            return (max(self.get_height(root.l), self.get_height(root.r)) + 1)

     
    #time-complexity = O(log n)           
    def get_node(self, root, key):

        if (root != None):
            if (root.value == key):
                return root
            elif key > root.value:
                return (self.get_node(root.r, key))
            else:
                return (self.get_node(root.l, key))
        else:
            return False

    #time-complexity = O(n)
    def get_bal(self,root):
        if root is None:
            return 
        return (self.get_height(root.l) - self.get_height(root.r))

    #time-complexity = O(n)
    def in_order(self, root):
        result = list()

        if root != None:
            result += self.in_order(root.l)
            result.append(root.value)
            result += self.in_order(root.r)

        return result




# You are requied return the the value of the root in a list after
# If Root is not Found then you are required to return None

    #time-complexity = O(log n)
    def get_left_most(self, root):

        while root.l != None:
            return self.get_left_most(root.l)
        
        return root


    #time-complexity = O(log n)
    def delete_node(self, root, node_to_be_deleted):
        if root != None:
            if root.value == node_to_be_deleted:
                if not(root.l or root.r):
                    #no children
                    return None
                elif root.l == None:
                    return root.r
                elif root.r == None:
                    return root.l
                else:
                    new_val = self.get_left_most(root.r).value
                    root.value = new_val
                    root.r = self.delete_node(root.r, new_val)
            elif node_to_be_deleted > root.value:
                root.r = self.delete_node(root.r, node_to_be_deleted)
            elif node_to_be_deleted < root.value:
                root.l = self.delete_node(root.l, node_to_be_deleted)
        else:
            return None

         # balancing
        root = self.balancer(root)

        return root


    #time-complexity = O(log n)
    def update_node(self,root, new_value_of_node,old_value_of_node):

        if self.get_node(root, old_value_of_node):
            self.get_node(root, old_value_of_node).value = new_value_of_node
        else:
            return False


    #time-complexity = O(n)
    def level_deleter(self, root, level, sea_level):
        
        if level == sea_level:
            root = self.delete_node(root, root.value)
        else:
            root.l = self.level_deleter(root.l, level, sea_level + 1) 
            root.r = self.level_deleter(root.r, level, sea_level + 1) 

        return root


    #time-complexity = O(n)
    def delete_all_nodes_at_given_height(self,root,level):
        if root is None:
            return
        return self.level_deleter(root , level, 0)

# Testing Area ---

# You can create a class tree object below and check the implementation of your functions.
# Make sure to comment out the code before running the tests else it might mix up the results.
# Create an object here to test the functions.

if __name__ == "__main__":
    
    TestTree = AVLTree()

    # r_root = TreeNode(5)
    # r_root.h = 3
    # r_root.l = TreeNode(4)
    # r_root.l.h = 2
    # r_root.l.l = TreeNode(3)
    # r_root.l.l.l = TreeNode(2)
    # r_root.l.l.h = 1
    # # r_root.r = TreeNode(6)

    # balanced = TestTree.balancer(r_root)
    # print(TestTree.in_order(balanced))
    # print(balanced.value)
    # print(balanced.r.value)
    new_root = None
    for i in range(1,32):
        new_root = TestTree.insert(new_root, i)

    root_val = new_root.value

    new_root = TestTree.delete_node(new_root, root_val)
    print(TestTree.in_order(new_root))





    
