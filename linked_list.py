class Node(object):
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
 
 
class DoubleList(object):
 
    def __init__(self):
    	self.head = None
    	self.tail = None
    	self.length = 0
 
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
 
    def remove(self, node_value):
        current_node = self.head
 
        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
 
            current_node = current_node.next
 
    def show(self):
        print "Show list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.prev.data if hasattr(current_node.prev, "data") else None,
            print current_node.data,
            print current_node.next.data if hasattr(current_node.next, "data") else None
 
            current_node = current_node.next
        print "*"*50

        current_node = self.head
        while current_node is not None:
        	print current_node.data
        	current_node = current_node.next
        print "*"*50

    def remove_duplicates(self):
		current_node = self.head
		traversed = {}
		while current_node is not None:
			if traversed.get(str(current_node.data), None) == None:
				traversed[str(current_node.data)] = current_node.data
			else:
				if current_node.prev == None:
					(current_node.next).prev = None
				elif current_node.next == None:
					(current_node.prev).next = None
				else:
					(current_node.prev).next = current_node.next
					(current_node.next).prev = current_node.prev
				self.length -= 1


			current_node = current_node.next

    def remove_k_from_end(self, k):
		current_node = self.tail
		print("tail", current_node)
		index = 0
		while index != self.length:
			if index == k:
				self.show()
				if current_node.prev == None:
					(current_node.next).prev = None
				elif current_node.next == None:
					(current_node.prev).next = None
				else:
					(current_node.prev).next = current_node.next
					(current_node.next).prev = current_node.prev
				self.length -= 1
				self.show()
				break
			else:
				print current_node.prev
				current_node = current_node.prev
				index += 1

    def remove_middle_node(self):
		current_node = self.head
		index = 0
		print("length", self.length)
		while index != ((self.length + 1) / 2):
			current_node = current_node.next
			index += 1
		if current_node.prev == None:
					(current_node.next).prev = None
		if current_node.next == None:
			(current_node.prev).next = None
		if current_node.next != None and current_node.prev != None:
			(current_node.prev).next = current_node.next
			(current_node.next).prev = current_node.prev
		self.length -= 1
		


 
 
d = DoubleList()
 
d.append(5)
d.append(6)
d.append(50)
d.append(30)
d.append(99)
d.append(101010)
d.append(23)
d.append(23)
d.append(5)
 
d.show()

print("***** made list ******")

# Questions

#### Remove duplicates

d.remove_duplicates()

d.show()


print("***** remove duplicates ******")


#### Delete kth to last node

d.remove_k_from_end(6)

d.show()

print("***** delete kth node ******")
#### Delete the middle node

d.remove_middle_node()

d.show()

print("***** delete middle node ******")
#### Partition list so that all nodes less than x come before and all node greater come after


#### create a method that takes two linked lists and returns the number created by joining the numbers in the nodes together in reverse order


#### check if list is a palindrome (same backwards as forwards)


#### determine if two linked lists are intersecting (not by value... the exact same node)


#### loop detection