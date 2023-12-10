class Node:
    def __init__(self, data=0):
        if -100 <= data <= 100: #store the data within the given range of number
            self.data = data
            self.next = None
        else:
            print("Enter number that ranges from -100 to 100")
            self.data = None  #doesn't store the data that exceeds
            self.next = None

def count(LinkedList):

    count_track = 0

    while LinkedList is not None:
        count_track += 1
        LinkedList = LinkedList.next

    return count_track

def merged_list(first_list, second_list):
    Newlist = Node() #empty linked list to be filled by first and second list
    current_node = Newlist #recent node to be accessed

    while first_list is not None and first_list.data is not None and second_list is not None and second_list.data is not None:

        if first_list.data <= second_list.data:
            current_node.next = first_list #current top node enters Newlist
            first_list = first_list.next #moves to the next node

        else:
            current_node.next = second_list  #current top node enters Newlist
            second_list = second_list.next #moves to the next node

        current_node = current_node.next  # move to the next node in the merged list

        #For the remaining node nothing to compare data with
        if first_list is not None:
            current_node.next = first_list
        elif second_list is not None:
            current_node.next = second_list

    if count(Newlist) > 50: 
        print("Overload of Node! Please adjust ur list")
        exit()
    else:
        return Newlist.next

#First list
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)

#Second list
list2 = Node(1)
list2.next = Node(3)
list2.next.next = Node(4)

#Execute Merging 2 Linked Lists
List1_2=merged_list(list1,list2)

#Print final result fo merged list
while List1_2 is not None:
    print(List1_2.data, end=" ")
    List1_2 = List1_2.next

