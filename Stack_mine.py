class Stack:
    def __init__(self):
        self.data = []
        
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def pop(self):
        if self.is_empty():
            print("the stack is empty")
        else:
            return self.data.pop(-1)
        
    def push(self, item):
        self.data.append(item)
        
    def peek(self):
        return self.data[0]
    
##############################################
#运行#########################################
##############################################

if __name__ == "__main__":
    bracket = {'(':')', '{':'}', '[':']'}
    stack = Stack()
    def  bracket_matching(string):
        for i in string:
            if i in '({[':
                stack.push(i)
            elif i in ')}]':
                if stack.is_empty():
                    print('the right bracket is more than the left')
                else:
                    top_char = stack.pop()
                    if bracket[top_char] != i:
                        print('the bracket is not corresponding')
        if stack.is_empty():
            print('the bracket is balance')
        else:
            print('the left bracket is more than the right')
            
    string = '({123[56]}468)[](){'
    bracket_matching(string)