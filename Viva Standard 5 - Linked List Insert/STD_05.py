changed = 0

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
        print(end="\n")

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)

    def AtEnd(self, newdata):
        if self.headval is None:
            self.headval = newdata
            return
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = newdata

    def findAndInsert(self, cur_val, val_before, new_val):
        global changed
        # First, this method find the last member of the SLinkedList. After that, a return command prompts the program
        # to start modifying
        if cur_val is None:
            return
        self.findAndInsert(cur_val.nextval, val_before, new_val)
        # Once the "bottom" has been found, we check to see where the recreate the SLinkedList until the
        # new date has been found. After that, we append it to the list and stop recreating it.
        if cur_val.nextval == val_before:
            new_val.nextval = cur_val.nextval
            cur_val.nextval = new_val
            changed = 1
        else:
            cur_val = cur_val.nextval
        # The reason why I went "down" in the list and remade it is because the way it's made we cannot access a
        # specific day unless we have a reference to it

    def Insert(self, val_before, newdata):
        global changed
        # The purpose of this function is to check if the type of val_before is node. If it is, it goes to
        # the findAndInsert() function which does the work. It additionally checks if any change has been made
        # to the List
        if not (isinstance(val_before, Node) and isinstance(newdata, Node)):
            print("At least one of the arguments passed is not of type node")
            return
        else:
            self.findAndInsert(self.headval, val_before, newdata)
            if changed == 0:
                print("Nothing has changed for the inputted information, one of the nodes has not been found")

            changed = 0




Mon = Node("Mon")
Tue = Node("Tue")
Wed = Node("Wed")
Thu = Node("Thu")
Fri = Node("Fri")
Sat = Node("Sat")
Sun = Node("Sun")


print("Test 1")
# The test that was required
list1 = SLinkedList()
list1.headval = Node("Mon")
list1.headval.nextval = Tue
Tue.nextval = Thu
Thu.nextval = Fri
Fri.nextval = Sat
list1.AtEnd(Sun)

list1.Insert(Thu, Wed)
list1.listprint()

# Testing the insert function, and we need to dereference the nextvalues

Mon.nextval=None
Tue.nextval=None
Wed.nextval=None
Thu.nextval=None
Fri.nextval=None
Sat.nextval=None
Sun.nextval=None


print("Test 2")
listN = SLinkedList()
listN.headval = Mon
listN.headval.nextval = Tue
listN.AtEnd(Sun)

# We Sunday, it works. When we try to insert Thursday it doesnt work because Wednesday is not part of the list
listN.Insert(Sun, Sat)
listN.listprint()
listN.Insert(Thu, Wed)
listN.listprint()
# After that we instert all the other days
listN.Insert(Sat, Fri)
listN.Insert(Fri, Thu)
listN.Insert(Thu, Wed)

listN.listprint()