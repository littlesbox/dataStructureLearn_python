#节点类
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#列表类        
class LinkList:
    def __init__(self):
        self.head = None
    
    #判断列表是不是空列表
    def is_None(self):
        if self.head == None:
            return True
        else:
            return False
    
    #遍历列表数据
    def print_everyone(self):
        if not self.is_None():
            current_node = self.head
            while current_node.next:
                print(current_node.data)
                current_node = current_node.next
            print(current_node.data)
        else:
            print('the linklist is empty')
    
    #头部插入
    def insert_front(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    #尾部插入
    def insert_end(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = newNode
            
    #删除第一个值为key的节点
    def delete_node(self, key):
        if not self.is_None():
            current_node = self.head
            pre_node = self.head
            if self.head.data == key:
                self.head = current_node.next
            else:
                while current_node.data != key:
                    pre_node = current_node
                    current_node = current_node.next
                if current_node:
                    pre_node.next = current_node.next
                    current_node.next = None
                else:
                    print(f"{key} is not in the list")
        else:
            print("the list is empty")
                
        

##############################
#运行#########################
##############################
if __name__ == '__main__':
    a = LinkList()
    for i in range(5):
        a.insert_end(i)