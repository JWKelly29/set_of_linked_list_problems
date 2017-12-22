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

    def partition_list(self, value):
		current_node = self.head
		before_start = None
		before_end = None
		middle_start = None
		middle_end = None
		after_start = None
		after_end = None
		index = 0
		current_node = self.head

		while index < self.length:
			next_node = current_node.next
			if current_node.data < value:
				if before_start == None and before_end == None:
					before_start = current_node
					before_start.prev = None
					before_start.next = None
					before_end   = current_node
					before_end.prev = None
					before_end.next = None
				else:
					current_node.prev = before_end
					current_node.next = None
					before_end.next = current_node
					before_end = current_node
			elif current_node.data > value:
				if after_start == None and after_end == None:
					after_start = current_node
					after_start.prev = None
					after_start.next = None
					after_end   = current_node
					after_end.prev = None
					after_end.next = None
				else:
					current_node.prev = after_end
					current_node.next = None
					after_end.next = current_node
					after_end = current_node
			else:
				if middle_start == None and middle_end == None:
					middle_start = current_node
					middle_start.prev = None
					middle_start.next = None
					middle_end   = current_node
					middle_end.prev = None
					middle_end.next = None
				else:
					current_node.prev = middle_end
					current_node.next = None
					middle_end.next = current_node
					middle_end = current_node
			current_node = next_node
			index += 1

		if before_end != None and middle_end != None and after_end != None:
			before_end.next = middle_start
			middle_start.prev = before_end
			middle_end.next = after_start
			after_start.prev = middle_end
			self.head = before_start
			self.tail = after_end
		if before_end == None and middle_end != None and after_end != None:
			middle_end.next = after_start
			after_start.prev = middle_end
			self.head = middle_start
			self.tail = after_end
		if before_end != None and middle_end != None and after_end == None:
			before_end.next = middle_start
			middle_start.prev = before_end
			self.head = before_start
			self.tail = middle_end
		if before_end != None and middle_end == None and after_end != None:
			before_end.next = after_start
			after_start.prev = before_end
			self.head = before_start
			self.tail = after_end

    def is_palin(self):
		# iterate through list from front and back. If node is the same all the way through return true else false
		head_to_tail = self.head
		tail_to_head = self.tail
		i = 0
		while i < self.length:
			if head_to_tail.data != tail_to_head.data:
				print "false"
				return False
			else:
				head_to_tail = head_to_tail.next
				tail_to_head = tail_to_head.prev
				i += 1
			if i == self.length - 1:
				print "true"
				return True



def join_two_numerical_lists(list1,list2):
	list_str_1 = ""
	list_str_2 = ""
	i = 0
	current_node = list1.tail
	while i < list1.length:
		list_str_1 += str(current_node.data)
		current_node = current_node.prev
		i += 1
	i = 0
	current_node = list2.tail
	while i < list2.length:
		list_str_2 += str(current_node.data)
		current_node = current_node.prev
		i += 1
	print(int(list_str_1) + int(list_str_2))
	return int(list_str_1) + int(list_str_2)









 
 
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

d.partition_list(30)

d.show()

print("***** Partitioned list ******")
#### create a method that takes two linked lists and returns the number created by joining the numbers in the nodes together in reverse order

dd = DoubleList()
dd.append(1)
dd.append(2)
dd.append(3)

ddd = DoubleList()
ddd.append(4)
ddd.append(5)
ddd.append(6)

join_two_numerical_lists(dd,ddd)



print("***** add number created by joining two linked lists ******")
#### check if list is a palindrome (same backwards as forwards)

palin = DoubleList()
palin.append(1)
palin.append(0)
palin.append(1)

not_palin = DoubleList()
not_palin.append(1)
not_palin.append(1)
not_palin.append(0)

palin.is_palin()

not_palin.is_palin()

print("***** check if list is a palindrome ******")
#### determine if two linked lists are intersecting (not by value... the exact same node)


#### loop detection