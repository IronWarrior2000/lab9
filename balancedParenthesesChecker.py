#Bill Nguyen | 11/22/24 | Lab 9

import queue
#PART 1 --------------------------------------------------------------
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
        
def isBalanced(expression):
    queue = Queue() #CREATE AN INSTANCE QUEUE 
     
    #VARIABLES CREATED FOR CHECKING THE QUEUE
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in expression: #FOR EACH CHARACTER IN EXPRESSION
        if char in opening: #IF THE CHARACTER IS IN OPENING 
            queue.enqueue(char) #IT WILL BE ADDED TO THE QUEUE
        elif char in closing: #IF ELSE CHARACTER IS IN CLOSING 
            if queue.isEmpty(): #IF THE QUEUE IS EMPTY
                return False #IT RETURN FALSE
            opening = queue.dequeue() #THE OPENING WILL BE THE NEW QUEUE
            if opening != matches[char]: #IF THE OPENING IS NOT IN MATCHES RETURN FALSE
                return False    
    
    return queue.isEmpty()
    

#TEST
expression1 = "({[]})"
expression2 = "{)}"
expression3 = "({}"
expression4 = "[({}])"


print(isBalanced(expression1))
print(isBalanced(expression2))
print(isBalanced(expression3))
print(isBalanced(expression4))


