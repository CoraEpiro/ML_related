import sys
import math    

class DynamicArray():
    def __init__(self):
        self.capacity = 1
        self.data = []
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def getcapacity(self):
        return self.capacity
    
    def append(self, obj):
        if self.size + 1 == self.capacity:
            
            
            #self.DoubleCapacity()
            
            self.EnlargeCapacity()
            
            
            new_data = []*self.capacity
            new_data = self.data.copy()
            self.data = new_data
        self.data.append(obj)
        self.size += 1
    
    def DoubleCapacity(self):
        self.capacity *= 2
        
    def EnlargeCapacity(self):
        self.capacity += math.ceil(self.capacity / 4)
    
    def getsizeof(self):
        return sys.getsizeof(self.data)


data = DynamicArray()
for k in range(100):
  a = len(data)
      
  capacity = data.getcapacity()
  
  b = data.getsizeof()
  print('Length: {0:3d}; Capacity: {1:3d}; Size in bytes: {2:4d}'.format(a, capacity, b))
  data.append(None)