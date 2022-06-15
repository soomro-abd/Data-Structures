from Part1 import LinkedList, Node
from Part2 import Stack, Queue

# Assignment 1-Part 3
# Applications of data structures

# The following function is provided to students already. Check manual for details
def find_vehicle_in_list(type_of_vehicle, Waiting):
    # Check if a bike is waiting
    if type_of_vehicle == "bike":
        if Waiting.head == None:
            return False
        else:
            traverse = Waiting.head
            while(traverse.data[0] != "b"):
                if(traverse.next == None):
                    return False
                traverse = traverse.next
            return traverse.data

    # Check if a car is waiting
    elif type_of_vehicle == "car": 
        if Waiting.head == None:
            return False
        else:
            traverse = Waiting.head
            while(traverse.data[0] != "c"):
                if(traverse.next == None):
                    return False
                traverse = traverse.next
            return traverse.data
    
    # Check if a truck is waiting
    elif type_of_vehicle == "truck":
        if Waiting.head == None:
            return False
        else:
            traverse = Waiting.head
            while(traverse.data[0] != "t"):
                if(traverse.next == None):
                    return False
                traverse = traverse.next
            return traverse.data

# To-do Function 1
# This function is called whenever a new vehicle comes to the toll plaza
def incoming_traffic(data, DS1, DS2, DS3, Waiting, tax_collection):

    # Write Code to cater to bikes
    if (data[0] == 'b'):
        if (DS1.get_length() < 5):
            DS1.enqueue(data)
            tax_collection["bike_total"] += 30
        else:
            Waiting.insert_at_tail(data)

    # Write Code to cater to cars
    if (data[0] == 'c'):
        if (DS2.get_length() < 5):
            DS2.enqueue(data)
            tax_collection["car_total"] += 50
        else:
            Waiting.insert_at_tail(data)


    # Write Code to cater to trucks
    if (data[0] == 't'):
        if (DS3.get_length() < 5):
            DS3.enqueue(data)
            tax_collection["truck_total"] += 100
        else:
            Waiting.insert_at_tail(data)

    

# To-do Function 2
def outgoing_traffic(type_of_vehicle, DS1, DS2, DS3, Waiting, tax_collection):

    if (type_of_vehicle == "bike"):
        # Remove a bike
        DS1.dequeue()
    elif (type_of_vehicle == "car"):
        # Remove a car
        DS2.dequeue()
    elif (type_of_vehicle == "truck"):
        # Remove a truck
        DS3.dequeue()

        
    while(DS1.get_length() < 5):
            # See if any vehicle of bike type has been waiting in the Waiting List. Use find_vehicle_in_list function for this.
            if (find_vehicle_in_list("bike", Waiting) != False):
                temp_data = find_vehicle_in_list("bike", Waiting)
                Waiting.delete_any(temp_data)
                incoming_traffic(temp_data, DS1, DS2, DS3, Waiting, tax_collection)
            else:
                break

    while(DS2.get_length() < 5):
            # See if any vehicle of car type has been waiting in the Waiting List. Use find_vehicle_in_list function for this.
            if (find_vehicle_in_list("car", Waiting) != False):
                temp_data = find_vehicle_in_list("car", Waiting)
                Waiting.delete_any(temp_data)
                incoming_traffic(temp_data, DS1, DS2, DS3, Waiting, tax_collection)
            else:
                break

    while(DS3.get_length() < 5):
            # See if any vehicle of truck type has been waiting in the Waiting List. Use find_vehicle_in_list function for this.
            if (find_vehicle_in_list("truck", Waiting) != False):
                temp_data = find_vehicle_in_list("truck", Waiting)
                Waiting.delete_any(temp_data)
                incoming_traffic(temp_data, DS1, DS2, DS3, Waiting, tax_collection)
            else:
                break

    



# To-do Function 3
def total_tax(tax_collection):
    values = tax_collection.values()
    return sum(values)

# def main():
#     # Total collected tax for each type of vehicle
#     tax_collection = {"bike_total": 0, "car_total": 0, "truck_total": 0}

#     # Initial three data structures here.
#     # First data structure should represent bikes
#     # Second data structure should represent cars
#     # Third data structure should represent trucks
    

#     # Initialize a linked list that holds all sorts of vehicles in order that they come but have to wait due to full data structures.
    
# #main()