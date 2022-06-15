# Assignment 2-Part 3
# Implemetation

from collections import deque


class Node:
	def __init__(self, value):
		self.value = value
		self.l = None
		self.r = None

#time-complexity = O(n)
def visiting_floors(root):
    
	#i learned this technique of level order traversal from the lecture
	if root is None:
		return

	result = []
	temp = []
	temp.append(root)

	while bool(temp):
		node = temp.pop(0)
		result.append(str(node.value))

		if node.l != None:
			temp.append(node.l)
		
		if node.r != None:
			temp.append(node.r)

	return result


#time-complexity = O(n)
def changing_helper(root, level):
	if root != None:
		if (level % 2 == 1):
			the_sum = (6 * pow(2, level - 1)) - 1
			root.value = the_sum - root.value
		
		root.l = changing_helper(root.l, level + 1)
		root.r = changing_helper(root.r, level + 1)
	else:
		return None

	return root
	

#time-complexity = O(n)
def changing_room_numbers(root):
	return changing_helper(root, 0)


if __name__ == '__main__':

	''' Construct the following tree
				  1
			   /     \
			 /         \
		   2             3
		 /   \         /   \
		4     5       6     7
	  /  \    / \    / \    / \
	 8    9  10 11 12  13  14 15
	'''

	root = Node(1)
	root.l = Node(2)
	root.r = Node(3)
	root.l.l = Node(4)
	root.l.r = Node(5)
	root.r.l = Node(6)
	root.r.r = Node(7)
	root.l.l.l = Node(8)
	root.l.l.r = Node(9)
	root.l.r.l = Node(10)
	root.l.r.r = Node(11)
	root.r.l.l = Node(12)
	root.r.l.r = Node(13)
	root.r.r.l = Node(14)
	root.r.r.r = Node(15)
# Call your functions below this line of code

	updated = changing_room_numbers(root)
	print(visiting_floors(updated))
