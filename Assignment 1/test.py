from Part1 import LinkedList, Node
from Part2 import Stack, Queue
from Part3 import find_vehicle_in_list, incoming_traffic, outgoing_traffic, total_tax

class Test(LinkedList):
   
    def test_function_incremental(self, var_x):
        meta_data = Node(var_x)
        meta_data.next = self.head
        self.head = meta_data

def test_get_head(points_part_one):
    print("Initializing Test 1 - Get Head")
    test = Test()
    try:
        if test.get_head() != None:
            print("Test 1 Failed! Cater to Empty Linked List " + str(points_part_one["score"]) + "/40 \n")
        else:
            test.test_function_incremental(1)
            test.test_function_incremental(2)
            if test.get_head() == 2:
                points_part_one["score"] += 2
                print("Test 1 Passed! " + str(points_part_one["score"]) + "/40 \n")
            else:
                print("Test 1 Failed! " + str(points_part_one["score"]) + "/40 \n")
    except:
        print("Test 1 Failed! Cater to empty Linked List " + str(points_part_one["score"]) + "/40 \n")

def test_get_tail(points_part_one):
    print("Initializing Test 2 - Get Tail")
    test = Test()
    try:
        if test.get_tail() != None:
            print("Test 2 Failed! Cater to Empty Linked List " + str(points_part_one["score"]) + "/40 \n")
        else:
            test.test_function_incremental(1)
            test.test_function_incremental(2)
            if test.get_tail() == 1:
                points_part_one["score"] += 2
                print("Test 2 Passed! " + str(points_part_one["score"]) + "/40 \n")
            else:
                print("Test 2 Failed! " + str(points_part_one["score"]) + "/40 \n")
    except:
        print("Test 2 Failed! Cater to empty Linked List " + str(points_part_one["score"]) + "/40 \n")

def test_if_empty(points_part_one):
    print("Initializing Test 3 - Empty Lists")
    test = Test()
    test.test_function_incremental('A')
    try:
        if test.is_empty() == False:
            points_part_one["score"] += 1
            print("Test 3 Passed! " + str(points_part_one["score"]) + "/40 \n") 
        else: 
            print("Test 3 Failed! " + str(points_part_one["score"]) + "/40 \n")
    except:
        print("Test 3 Failed! " + str(points_part_one["score"]) + "/40 \n")

def test_insert_at_head(points_part_one):
    print("Initializing Test 4 - Insert at Head")
    test = Test()
    test.insert_at_head('A')
    try:
        if test.head.data == 'A':
            pass
        else: 
            print("Test 4 Failed!" + str(points_part_one["score"]) + "/40 \n") 
            return
        if test.print_list() == ['A']:
            pass
        else: 
            print("Test 4 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
        
        test.insert_at_head('B')
        test.insert_at_head('C')
        if test.head.data == 'C' and test.print_list() == ['C', 'B', 'A']:
            points_part_one["score"] += 4
            print("Test 4 Passed! " + str(points_part_one["score"]) + "/40 \n") 
        else: 
            print("Test 4 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
    except:
        print("Test 4 Failed! " + str(points_part_one["score"]) + "/40 \n")
        return

def test_insert_at_tail(points_part_one):
    print("Initializing Test 5 - Insert at Tail")
    test = Test()
    test.insert_at_tail('A')
    try:
        if test.head.data == 'A':
            pass
        else: 
            print("Test 5 Failed!" + str(points_part_one["score"]) + "/40 \n") 
            return
        if test.print_list() == ['A']:
            pass
        else: 
            print("Test 5 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
        
        test.insert_at_tail('B')
        test.insert_at_tail('C')
        if test.head.data == 'A' and test.print_list() == ['A', 'B', 'C']:
            points_part_one["score"] += 4
            print("Test 5 Passed! " + str(points_part_one["score"]) + "/40 \n") 
        else: 
            print("Test 5 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
    except:
        print("Test 5 Failed! " + str(points_part_one["score"]) + "/40 \n")
        return

def test_insert_in_between(points_part_one):
    print("Initializing Test 6 - Insert in Between")
    test = Test()
    test.test_function_incremental(1)
    test.test_function_incremental(5)
    test.test_function_incremental(17)
    test.test_function_incremental(23)
    test.test_function_incremental(34)
    test.test_function_incremental(55)
    test.insert_in_between('test', 17, 5)
    try:
        if test.print_list() == [55, 34, 23, 17, 'test', 5, 1]:
            points_part_one["score"] += 5
            print("Test 6 Passed! " + str(points_part_one["score"]) + "/40 \n") 
        else: 
            print("Test 6 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
    except:
        print("Test 6 Failed! " + str(points_part_one["score"]) + "/40 \n")
        return

def test_delete_head(points_part_one):
    print("Initializing Test 7 - Delete Head")
    test = Test()
    try:
        test.test_function_incremental('A')
        test.test_function_incremental('B')
        test.test_function_incremental('C')
        test.delete_head()
        if test.head.data == 'B' and test.print_list() == ['B', 'A']:
            pass
        else: 
            print("Test 7 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
        test.delete_head()
        test.delete_head()
        if test.head == None:
            points_part_one["score"] += 2
            print("Test 7 Passed! " + str(points_part_one["score"]) + "/40 \n") 
    except:
        print("Test 7 Failed! " + str(points_part_one["score"]) + "/40 \n")
        return

def test_delete_tail(points_part_one):
    print("Initializing Test 8 - Delete Tail")
    test = Test()
    try:
        test.test_function_incremental('A')
        test.test_function_incremental('B')
        test.test_function_incremental('C')
        test.delete_tail()
        if test.head.data == 'C' and test.print_list() == ['C', 'B']:
            pass
        else: 
            print("Test 8 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
        test.delete_tail()
        test.delete_tail()
        if test.head == None:
            points_part_one["score"] += 2
            print("Test 8 Passed! " + str(points_part_one["score"]) + "/40 \n") 
    except:
        print("Test 8 Failed! " + str(points_part_one["score"]) + "/40 \n")
        return

def test_delete_any(points_part_one):
    print("Initializing Test 9 - Delete Any")
    test = Test()
    try:
        test.test_function_incremental('A')
        test.test_function_incremental('B')
        test.test_function_incremental('C')
        test.test_function_incremental('D')
        test.test_function_incremental('E')
        test.test_function_incremental('F')
        test.delete_any('F')
        if test.head.data == 'E' and test.print_list() == ['E', 'D', 'C', 'B', 'A']:
            pass
        else: 
            print("Test 9 Failed!" + str(points_part_one["score"]) + "/40 \n") 
            return
        test.delete_any('C')
        if test.print_list() == ['E', 'D', 'B', 'A']:
            pass
        else: 
            print("Test 9 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
        test.delete_any('E')
        test.delete_any('B')
        test.delete_any('A')
        test.delete_any('D')
        if test.head == None:
            points_part_one["score"] += 5
            print("Test 9 Passed! " + str(points_part_one["score"]) + "/40 \n") 
    except:
        print("Test 9 Failed! " + str(points_part_one["score"]) + "/40 \n")
        return

def test_get_length(points_part_one):
    print("Initializing Test 10 - Get Length")
    test = Test()
    try:
        if test.get_length() == 0:
            pass
        else: 
            print("Test 10 Failed!" + str(points_part_one["score"]) + "/40 \n") 
            return
        test.test_function_incremental('A')
        test.test_function_incremental('B')
        test.test_function_incremental('C')
        test.test_function_incremental('D')
        test.test_function_incremental('E')
        test.test_function_incremental('F')
        if test.get_length() == 6:
            points_part_one["score"] += 3
            print("Test 10 Passed! " + str(points_part_one["score"]) + "/40 \n") 
        else: 
            print("Test 10 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
    except:
        print("Test 10 Failed! " + str(points_part_one["score"]) + "/40 \n")
        return

def test_get_element(points_part_one):
    print("Initializing Test 11 - Get Element")
    test = Test()
    try:
        test.test_function_incremental('A')
        test.test_function_incremental('B')
        test.test_function_incremental('C')
        test.test_function_incremental('D')
        test.test_function_incremental('E')
        test.test_function_incremental('F')
        if test.get_element('Z') == False:
            pass
        else: 
            print("Test 11 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
        if test.get_element('E') == 'E':
            points_part_one["score"] += 4
            print("Test 11 Passed! " + str(points_part_one["score"]) + "/40 \n") 
        else: 
            print("Test 11 Failed!" + str(points_part_one["score"]) + "/40 \n") 
            return
    except:
        print("Test 11 Failed! " + str(points_part_one["score"]) + "/40 \n")
        return

def test_reverse(points_part_one):
    print("Initializing Test 12 - Reverse List")
    test = Test()
    try:
        test.test_function_incremental('A')
        test.reverse_list()
        if test.head.data =='A' and test.print_list() == ['A']:
            pass
        else: 
            print("Test 12 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
        test.test_function_incremental('B')
        test.test_function_incremental('C')
        test.test_function_incremental('D')
        test.test_function_incremental('E')
        test.test_function_incremental('F')
        test.reverse_list()
        if test.print_list() == ['A', 'B', 'C', 'D', 'E', 'F']:
            points_part_one["score"] += 6
            print("Test 12 Passed! " + str(points_part_one["score"]) + "/40 \n") 
        else: 
            print("Test 12 Failed! " + str(points_part_one["score"]) + "/40 \n") 
            return
    except:
        print("Test 12 Failed! " + str(points_part_one["score"]) + "/40 \n")
        return

points_part_one ={"score":0}

print("-----------------------------------")
print("Testing Implementation of Part 1... \n")
test_get_head(points_part_one)
test_get_tail(points_part_one)
test_if_empty(points_part_one)
test_insert_at_head(points_part_one)
test_insert_at_tail(points_part_one)
test_insert_in_between(points_part_one)
test_delete_head(points_part_one)
test_delete_tail(points_part_one)
test_delete_any(points_part_one)
test_get_length(points_part_one)
test_get_element(points_part_one)
test_reverse(points_part_one)

print("Total for Part 1: " + str(points_part_one["score"]) + "/40 \n")

class Test2(Stack, Queue):
    def test_function_incremental(self, var_x):
        meta_data = Node(var_x)
        meta_data.next = self.head
        self.head = meta_data

def test_top(points_stack):
    print("Initializing Test 1 - Top")
    cap = 3
    test = Test2(cap)
    try:
        if test.top() != None:
            print("Test 1 Failed!" + str(points_stack["score"]) + "/10 \n")
        else:
            test.test_function_incremental(1)
            test.test_function_incremental(2)
            test.test_function_incremental(3)
            if test.top() == 3:
                points_stack["score"] += 2
                print("Test 1 Passed! " + str(points_stack["score"]) + "/10 \n")
            else:
                print("Test 1 Failed! " + str(points_stack["score"]) + "/10 \n")
    except:
        print("Test 1 Failed! Cater to an empty Stack " + str(points_stack["score"]) + "/10 \n")

def test_push(points_stack):
    print("Initializing Test 2 - Push")
    cap = 3 
    test = Test2(cap)
    test.push('A')
    try:
        if test.head.data == 'A':
            pass
        else: 
            print("Test 2 Failed!" + str(points_stack["score"]) + "/10 \n") 
            return
        if test.print_list() == ['A']:
            pass
        else: 
            print("Test 2 Failed! " + str(points_stack["score"]) + "/10 \n") 
            return

        test.push('B')
        test.push('C')
            
        if test.head.data == 'C' and test.print_list() == ['C', 'B', 'A']:
            points_stack["score"] += 3
        else: 
            print("Test 2 Failed! " + str(points_stack["score"]) + "/10 \n") 
            return
        
        test.push('D') 
        if test.get_length() > cap: 
            print("Cater to Stack Capacity condition to gain full marks " + str(points_stack["score"]) + "/10 \n")
        else: 
            points_stack["score"] += 3 
            print("Test 2 Passed! " + str(points_stack["score"]) + "/10 \n") 
    except:
        print("Test 2 Failed! " + str(points_stack["score"]) + "/10 \n")
        return


def test_pop(points_stack):
    print("Initializing Test 3 - Pop")
    cap = 3
    test = Test2(cap)
    try:
        if test.pop() != None:
            print("Test 3 Failed!" + str(points_stack["score"]) + "/10 \n")
        else:
            test.test_function_incremental("A")
            test.test_function_incremental("B")
            test.test_function_incremental("C")
            test.pop()
            if test.head.data == 'B' and test.print_list() == ['B', 'A']:
                points_stack["score"] += 2
                print("Test 3 Passed! " + str(points_stack["score"]) + "/10 \n")
            else:
                print("Test 3 Failed! " + str(points_stack["score"]) + "/10 \n")
    except:
        print("Test 3 Failed! Cater to an empty Stack " + str(points_stack["score"]) + "/10 \n")


def test_enqueue(points_queue):
    print("Initializing Test 1 - Enqueue")
    cap = 3 
    test = Test2(cap)
    test.enqueue('A')
    try:
        if test.head.data == 'A':
            pass
        else: 
            print("Test 2 Failed!" + str(points_queue["score"]) + "/10 \n") 
            return
        if test.print_list() == ['A']:
            pass
        else: 
            print("Test 2 Failed! " + str(points_queue["score"]) + "/10 \n") 
            return

        test.enqueue('B')
        test.enqueue('C')
       
        if test.head.data == 'A' and test.print_list() == ['A', 'B', 'C']:
            points_queue["score"] += 2
        else: 
            print("Test 2 Failed! " + str(points_queue["score"]) + "/20 \n") 
            return
        
        test.enqueue('D')
        if test.get_length() > cap: 
            print("Cater to Queue Capacity condition to gain full marks " + str(points_queue["score"]) + "/10 \n")
        else: 
            points_queue["score"] += 1 
            print("Test 2 Passed! " + str(points_queue["score"]) + "/10 \n") 
    except:
        print("Test 2 Failed! " + str(points_queue["score"]) + "/10 \n")
        return

def test_dequeue(points_queue):
    print("Initializing Test 3 - Dequeue")
    cap = 3
    test = Test2(cap)
    try:
        if test.dequeue() != None:
            print("Test 3 Failed!" + str(points_queue["score"]) + "/10 \n")
        else:
            test.test_function_incremental("C")
            test.test_function_incremental("B")
            test.test_function_incremental("A")
            test.dequeue()
            if test.head.data == 'B' and test.print_list() == ['B', 'C']:
                points_queue["score"] += 3 
                print("Test 3 Passed! " + str(points_queue["score"]) + "/10 \n")
            else:
                print("Test 3 Failed! " + str(points_queue["score"]) + "/10 \n")
    except:
        print("Test 3 Failed! Cater to an empty queue " + str(points_queue["score"]) + "/10 \n")

def test_get_front(points_queue):
    print("Initializing Test 3 - Get Front")
    cap = 3
    test = Test2(cap)
    try:
        if test.get_front() != None:
            print("Test 3 Failed!" + str(points_queue["score"]) + "/10 \n")
        else:
            test.test_function_incremental("A")
            test.test_function_incremental("B")
            test.test_function_incremental("C")
            if test.get_front() == 'C' and test.print_list() == ['C','B', 'A']:
                points_queue["score"] += 2
                print("Test 3 Passed! " + str(points_queue["score"]) + "/10 \n")
            else:
                print("Test 3 Failed! " + str(points_queue["score"]) + "/10 \n")
    except:
        print("Test 3 Failed! Cater to an empty Queue " + str(points_queue["score"]) + "/10 \n")

def test_get_rear(points_queue):
    print("Initializing Test 4 - Get Rear")
    cap = 3
    test = Test2(cap)
    try:
        if test.get_rear() != None:
            print("Test 4 Failed!" + str(points_queue["score"]) + "/10 \n")
        else:
            test.test_function_incremental("A")
            test.test_function_incremental("B")
            test.test_function_incremental("C")
            if test.get_rear() == 'A' and test.print_list() == ['C','B', 'A']:
                points_queue["score"] += 2
                print("Test 4 Passed! " + str(points_queue["score"]) + "/10 \n")
            else:
                print("Test 4 Failed! " + str(points_queue["score"]) + "/10 \n")
    except:
        print("Test 4 Failed! Cater to an empty Queue " + str(points_queue["score"]) + "/10 \n")

print("-----------------------------------")
print("Testing Implementation of Part 2... \n")

points_stack ={"score":0}
points_queue ={"score":0}
print("Testing Stack... \n")
test_top(points_stack) # 2 marks 
test_push(points_stack) # 6 marks 
test_pop(points_stack) # 2 marks 
print("Testing Queue... \n")
test_enqueue(points_queue) # 3 marks 
test_dequeue(points_queue) # 3 marks 
test_get_front(points_queue) # 2 marks 
test_get_rear(points_queue) # 2 marks 
total_part2 = points_queue["score"] + points_stack["score"]
print("Total for Part 2: " + str(total_part2) + "/20 \n")

def test_direct_traffic(points_part_three):
    print("Initializing Test 1 - Directing Incoming Traffic Flow")
    tax_collection = {"bike_total": 0, "car_total": 0, "truck_total": 0}
    Queue1 = Queue(5)
    Queue2 = Queue(5)
    Queue3 = Queue(5)
    waiting = LinkedList()
    incoming_traffic("b_1", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_2", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_17", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_21", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    try:
        if Queue1.print_list() == ['b_1', 'b_2', 'b_3', 'b_4', 'b_5']:
            pass
        else:
            print("Test 1 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
        if Queue2.print_list() == ['c_3', 'c_4', 'c_5', 'c_6']:
            pass
        else:
            print("Test 1 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
        if Queue3.print_list() == ['t_4', 't_5', 't_6', 't_17', 't_21']:
            points_part_three["score"] += 10
            print("Test 1 Passed! " + str(points_part_three["score"]) + "/40 \n")
        else:
            print("Test 1 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
    except:
        print("Test 1 Failed! " + str(points_part_three["score"]) + "/40 \n")

def test_waiting_list(points_part_three):
    print("Initializing Test 2 - Store in Waiting List")
    tax_collection = {"bike_total": 0, "car_total": 0, "truck_total": 0}
    Queue1 = Queue(5)
    Queue2 = Queue(5)
    Queue3 = Queue(5)
    waiting = LinkedList()
    incoming_traffic("b_1", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_2", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_14", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_15", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_16", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_26", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_17", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_21", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_55", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_66", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_11", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_45", Queue1, Queue2, Queue3, waiting, tax_collection)
    try:
        if waiting.print_list() == ['b_6', 'c_15', 'b_16', 'b_26', 't_55', 't_66', 't_11', 'c_45']:
            points_part_three["score"] += 10
            print("Test 2 Passed! " + str(points_part_three["score"]) + "/40 \n")
        else:
            print("Test 2 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
        
    except:
        print("Test 2 Failed! " + str(points_part_three["score"]) + "/40 \n")

def test_outflow_traffic(points_part_three):
    print("Initializing Test 3 - Directing Outgoing Traffic Flow")
    tax_collection = {"bike_total": 0, "car_total": 0, "truck_total": 0}
    Queue1 = Queue(5)
    Queue2 = Queue(5)
    Queue3 = Queue(5)
    waiting = LinkedList()
    incoming_traffic("b_1", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_2", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("bike", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("bike", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("car", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("truck", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("truck", Queue1, Queue2, Queue3, waiting, tax_collection)
    try:
        if Queue1.print_list() == ['b_3', 'b_5']:
            pass
        else:
            print("Test 3 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
        if Queue2.print_list() == ['c_4', 'c_5', 'c_6']:
            pass
        else:
            print("Test 3 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
        if Queue3.print_list() == ['t_6']:
            points_part_three["score"] += 5
            print("Test 3 Passed! " + str(points_part_three["score"]) + "/40 \n")
        else:
            print("Test 3 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
    except:
        print("Test 3 Failed! " + str(points_part_three["score"]) + "/40 \n")

def test_bring_back(points_part_three):
    print("Initializing Test 4 - From Waiting List to Plaza")
    tax_collection = {"bike_total": 0, "car_total": 0, "truck_total": 0}
    Queue1 = Queue(5)
    Queue2 = Queue(5)
    Queue3 = Queue(5)
    waiting = LinkedList()
    incoming_traffic("b_1", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_2", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_1", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_2", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_1", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_2", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_7", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_8", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_7", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_7", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("bike", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("bike", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("car", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("truck", Queue1, Queue2, Queue3, waiting, tax_collection)
    try:
        if Queue1.print_list() == ['b_3', 'b_4', 'b_5', 'b_6', 'b_7']:
            pass
        else:
            print("Test 4 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
        if Queue2.print_list() == ['c_2', 'c_3', 'c_4', 'c_5', 'c_6'] and Queue3.print_list() == ['t_2', 't_3', 't_4', 't_5', 't_6']:
            pass
        else:
            print("Test 4 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
        if waiting.print_list() == ['b_8', 't_7', 'c_7']:
            points_part_three["score"] += 10
            print("Test 4 Passed! " + str(points_part_three["score"]) + "/40 \n")
        else:
            print("Test 4 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
    except:
        print("Test 4 Failed! " + str(points_part_three["score"]) + "/40 \n")

def test_total_tax(points_part_three):
    print("Initializing Test 5 - Calculate Total Tax")
    tax_collection = {"bike_total": 0, "car_total": 0, "truck_total": 0}
    Queue1 = Queue(5)
    Queue2 = Queue(5)
    Queue3 = Queue(5)
    waiting = LinkedList()
    incoming_traffic("b_1", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_2", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_1", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_2", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_1", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_2", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_7", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("b_8", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_3", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_4", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_5", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_6", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("t_7", Queue1, Queue2, Queue3, waiting, tax_collection)
    incoming_traffic("c_7", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("bike", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("bike", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("car", Queue1, Queue2, Queue3, waiting, tax_collection)
    outgoing_traffic("truck", Queue1, Queue2, Queue3, waiting, tax_collection)
    try:
        if tax_collection["bike_total"] == 210 and tax_collection["car_total"] == 300 and tax_collection["truck_total"] == 600:
            pass
        else:
            print("Test 5 Failed! " + str(points_part_three["score"]) + "/40 \n")
            return
        if total_tax(tax_collection) == 1110:
            points_part_three["score"] += 5
            print("Test 5 Passed! " + str(points_part_three["score"]) + "/40 \n")
            return
        else:
            print("Test 5 Failed! " + str(points_part_three["score"]) + "/40 \n")
            
    except:
        print("Test 5 Failed! " + str(points_part_three["score"]) + "/40 \n")

print("-----------------------------------")
print("Testing Implementation of Part 3... \n")
points_part_three ={"score":0}

test_direct_traffic(points_part_three)
test_waiting_list(points_part_three)
test_outflow_traffic(points_part_three)
test_bring_back(points_part_three)
test_total_tax(points_part_three)
print("Total for Part 3: " + str(points_part_three["score"]) + "/40 \n")
print("-----------------------------------")

print("Part 1 : " + str(points_part_one["score"]) + "/40 \n")
print("Part 2 : " + str(total_part2) + "/20 \n")
print("Part 3 : " + str(points_part_three["score"]) + "/40 \n")
print("Total Marks : " + str(points_part_one["score"] + total_part2 + points_part_three["score"])  + "/100 \n")

