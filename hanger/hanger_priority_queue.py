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
Binary Min Heap: 

Essentially LIST, kind of a tree. Smallest values float up to root (index 1). 
UN-USED 0 index. Parents always smaller than children.

-No pointers, just index. 2*i = lc, 2*i + 1 = rc, i // 2 = parent. Root = 1
-On Insert, new value appended, then perc up
-On del_min, min (root) value returned, last value in list moved to root, perc down
-Always update size!

1) Constructor: head list, size
2) Insert, del_min
3) Perc Up, Perc Down
4) Min Child

'''
from datetime import datetime

class priority_queue():

    # 1) Constructor: headlist, size
    def __init__(self):
        self.head_list = [0]
        self.size = 0



    # 2) insert, del_min

    def insert(self,data):

        # 1) append to list, 
        # 2) increment size, 
        # 3) perc up new value

        self.head_list.append(data)
        self.size += 1
        self.perc_up(self.size)

    
    def del_min(self):
        # 1) save root
        # 2) copy last value in list to root, pop last value, size -= 1
        # 3) perc down new root
        if self.size == 1:
            # if priority queue is empty, report that
            return None

        saved = self.head_list[1]                              # save root value

        self.head_list[1] = self.head_list[self.size]          # copy last value to root
        self.head_list.pop()                                   # pop last value
        self.size -= 1                                         # deincriment size
        
        self.perc_down(1)                                      # perc down new root
        return saved



    # 3) Perc Up, Perc Down

    def perc_up(self,i):
        # 1) While not root, 
        # 2) if parent > child, swap. 
        # 3 )Move index to parent.

        while i // 2 > 0:      # while not root

            # parent > child? swap
            if self.head_list[i//2].last_worn > self.head_list[i].last_worn:      
                tmp = self.head_list[i//2]                 # save parent
                self.head_list[i//2] = self.head_list[i]   # set parent to child
                self.head_list[i] = tmp                    # set child to tmp
            i = i // 2                                     # move up to the parent

    def perc_down(self,i):
        # 1) i * 2 is still in list (child exists)
        # 2) min child < i? swap
        # 3) set i to min child index

        while (i * 2 <= self.size):
            mc = self.min_child(i)

            # if min child val smaller than current
            if self.head_list[mc].last_worn < self.head_list[i].last_worn:     
                tmp = self.head_list[i]                    # swap
                self.head_list[i] = self.head_list[mc]
                self.head_list[mc] = tmp
            i = mc                                         # set to min child index


    def min_child(self,i):
        # 1) no rc? return lc
        # 2) lc < rc? return lc
        # 3) lc > rc, return rc

        if self.size < (2*i+1):            # if theres no rc
            return 2 * i                   # return lc
        else:
            #if lc < rc, return lc
            if self.head_list[2*i].last_worn < self.head_list[2*i + 1].last_worn:   
                return 2 * i
            else:   
                return 2*i + 1             # since lc > rc, return rc.

