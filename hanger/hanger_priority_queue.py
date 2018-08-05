## Hanger - Priority Queue - Min Heap

'''
Hanger Priority Queue - min heap, using datetime.datetime. Datetime supports the 
syntax:

past = datetime.now()
present = datetime.now()

past < present
>> True

So, that's how items will be ranked. 

Template needs a couple of modifications - since this ranks article instances,
need to check article.last_worn for the comparisons, not just the data's 'value'

Note that min_heap does not gaurentee sorted list throughout - just that you can 
pop the minimum item cheaply off the top.

Template: 
Queue

'''
from datetime import datetime

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def time_sort(self):
        self.items = self._mergesort(self.items)

        ''' 
merge sort:

1) base case
2) Save recursive call on L, R
3) Add smaller value from each side to temp list using pos indicies, Result
4) Add remaining
5) Return result

'''

    def _mergesort(self,x):

        # 1) base case (array size)
        
        if len(x) < 2:
            return x
        
        # 2) Call recursives on L, R

        mid = len(x) // 2
        
        left_half = self._mergesort(x[:mid])
        right_half = self._mergesort(x[mid:])

        #3) Add smaller value from each side to RESULT using pos indicies

        result = []
        i = 0
        j = 0

        while i < len(left_half) and j < len(right_half):
            
            #this line might not have datetime implicitly, come back to this
            if left_half[i].last_worn > right_half[j].last_worn:
                result.append(right_half[j])
                j += 1
            else:
                result.append(left_half[i])
                i += 1

        # 4) Add remaining elements

        result += left_half[i:]
        result += right_half[j:]

        # 5) return RESULT
        return result
