class Stack:

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next'            # streamline memory

    def __init__(self, element, next):            # initialize node's fields
      self._element = element         
      self._next = next                                 # next node reference

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty Stack."""
    self._start = None
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  def push(self, e):
    newest = self._Node(e, self._start)
    self._start = newest
    self._size += 1

  def pop(self):
    if self.is_empty():
       raise ValueError("Popping from an empty stack...")
    element = self._start._element
    next = self._start._next
    self._start._next = self._start._element = None
    self._start = next
    self._size -= 1
    return element                                      # return deleted element

  def reverse_list(self, new_list):
    reverse_list = []
    for element in new_list:
        self.push(element)
    start = self._start
    for i in range(self._size):
        reverse_list.append(start._element)
        start = start._next
    new_list = reverse_list
    return new_list
    

  def all_subsets(self, arr):
    subsets = [[]]
    
    for item in arr:
        self.push(item)
        
    while self._size != 0:
        element = self.pop()
        lenght = len(subsets)
        for index in range(lenght):
            new_subset = subsets[index].copy()
            new_subset.append(element)
            subsets.append(new_subset)
            
    return subsets


arr = [1, 2, 3]
stack = Stack()
print(stack.all_subsets(arr))

