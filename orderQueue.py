#Bill Nguyen | 11/22/24 | Lab 9

import queue
#PART 2 --------------------------------------------------------------
class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self): #CHECK IF ALL OF THE QUEUE IS EMPTY
        return len(self.queue) == 0
    
    def enqueue(self, item): #ADD ITEM TO THE QUEUE
        self.queue.append(item)

    def dequeue(self): #REMOVE ITEMS FROM THE QUEUE
        if not self.isEmpty(): #IF QUEUE IS NOT EMPTY IT WILL POP THE FIRST OBJECT IN QUEUE
            return self.queue.pop(0)
        else:
            return None
    
    def peek(self):
        if not self.isEmpty(): #WILL PEEK INTO THE QUEUE
            return self.queue[-1]
        else:
            return None
        
def simulatePrintQueue(jobs):
    queue = Queue() #CREATE AN INSTANCE QUEUE 
    
    print("---Queued Jobs---")
    for each in jobs:
        queue.enqueue(each)
        print(f"{each}")
    print("---Dequeued Jobs---")
    while not queue.isEmpty():
        current = queue.dequeue()
        print(f"{current}")
        
jobs = ["Test 1", "Test 2", "Test 3", "Test 4", "Test 5", "Test 6", "Test 7"]
simulatePrintQueue(jobs)