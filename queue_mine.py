from collections import deque

class queue:
    def __init__(self):
        self.dq = deque()
        
    def enqueue(self, data):
        self.dq.append(data)
        
    def dequeue(self):
        return self.dq.popleft()
    
    def peek(self):
        print(self.dq[0])
        
    def is_empty(self):
        if len(self.dq) == 0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.dq)
        
        
##########################################
#运行#####################################
##########################################
if __name__ == '__main__':
    q = queue()
    tasklist = ['task1', 'task2', 'task3','task4']
    for item in tasklist:
        q.enqueue(item)
        print(f'{item} joins the print task list')
    
    print("printer begining")
    while not q.is_empty():
        task = q.dequeue()
        print(f"{task} has printed")
        
    print("All tasks are done")