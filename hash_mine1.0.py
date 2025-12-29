'''
   嵌套的2层列表来实现链地址法的哈希表，
   键 映射到第一层的索引（通过定义的hash函数）
   第一次的索引对应的还是一个列表，称为bucket（桶）
   桶中存放的元组（键，值）
   如果hash函数映射的索引冲突了就在桶里面通过（键，值）来确定后续操作
   
   这个程序中的哈希函数很简单，要求键是字符串
   
   状态码：
   {'is_empty':0,
    'key_not_exist':-1,
    'normal':1}
'''
class HashTableChain:
    def __init__(self,table_size):
        self.table_size = table_size
        self.table = [[] for _ in range(table_size)]
    
    # 定义一个哈希函数，目前这个哈希函数很简单，接收字符串作为键
    def hashfunc(self, key):
        total = 0
        for char in key:
            total += ord(char)
        index = total % self.table_size
        return index
    
    def status_code2str(self, status_code):
        if status_code == 0:
            print("This table is empty!")
        elif status_code == -1:
            print("The specified key is not found!")
    
    def is_empty(self):
        total = 0
        for item in self.table:
            total += len(item)
        if total == 0:
            return True
        else:
            return False
        
    def insert(self, key, value):
        #首先根据key确定桶的索引
        index = self.hashfunc(key)
        #取出该桶，并检查当前键值对是否已经在桶中
        #如果在桶中则更改，否则添加
        bucket = self.table[index]
        exist_id = -1
        for i in range(len(bucket)):
            #桶中的元素是元组(key,value)
            if bucket[i][0] == key:
                exist_id = i
                break
        if exist_id != -1:
            bucket[exist_id] = (key,value)
        else:
            bucket.append((key,value))
        
    def display(self):
        status_code = 0
        if not self.is_empty():
            status_code = 1
            for i in range(len(self.table)):
                bucket = self.table[i]
                for item in bucket:
                    print(f"index:{i} key-value:{item}")
        return status_code
    
    def delete(self, key):
        status_code = 0
        if not self.is_empty():
            status_code = -1
            index = self.hashfunc(key)
            bucket = self.table[index]
            delete_id = 0
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    status_code = 1
                    delete_id = i
                    break
            bucket.pop(delete_id)
        return status_code
            
    def get(self, key):
        status_code = 0
        if not self.is_empty():
            status_code = -1
            index = self.hashfunc(key)
            bucket = self.table[index]
            for item in bucket:
                if item[0] == key:
                    status_code = 1
                    return item[1],status_code
        return None,status_code
        
     
#############################################
#运行########################################
#############################################
if __name__ == "__main__":
    a = ['Alice', 'Bob', 'Kevin']
    hashtable = HashTableChain(5)