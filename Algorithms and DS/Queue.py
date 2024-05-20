class Queue:

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:

    def __init__(self, element):            # initialize node's fields
      self._element = element         
      self._next = None

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty Queue."""
    self._start = None
    self._tail = None
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  def enqueue(self, e):
    newest = self._Node(e)
    
    if self._size == 0:
        self._start = newest
        self._tail = newest
    else:
        self._tail._next = newest
        self._tail = newest
        
    self._size += 1

  def dequeue(self):
    if self.is_empty():
       raise ValueError("Popping from an empty queue...")
    element = self._start._element
    self._start = self._start._next
    self._size -= 1
    return element                                      # return deleted element

  def all_subsets(self, arr):
    subsets = [[]]
    
    for item in arr:
        self.enqueue(item)
    
    while self._size != 0:
        element = self.dequeue()
        length = len(subsets)
        for index in range(length):
            new_subset = subsets[index].copy()
            new_subset.append(element)
            subsets.append(new_subset)
    
    return subsets
            

arr = [1, 2, 3]
queue = Queue()
print(queue.all_subsets(arr))
            
    