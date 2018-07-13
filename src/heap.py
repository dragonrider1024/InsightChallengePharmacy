#! /usr/bin/python
from drug import Drug

class MaxHeap:
    '''maximum heap data structure with siftup and siftdown and key index dictionary and its operation'''

    def __init__(self):
	'''Create an Empty Heap'''
        self.hq=[]
        self.n=0
	self.mapItemtoHeapIndex = {}

    def heappush(self,item):
	''' push and item to heap, and update the itemHeapIndex dictionary'''
	self.hq.append(item)
	self.mapItemtoHeapIndex[item]=self.n
	self.sift_up(self.n)
	self.n += 1
	return

    def __len__(self):
	''' size of the maxheap'''
	return self.n

    def sift_up(self,pos):
        ''' move the item up, after the heap key has been increased, and update the itemHeapIndex dictionary'''
	item=self.hq[pos]
	while pos>0:
	   parentpos=(pos-1)>>1
	   parent=self.hq[parentpos]
	   #print item, parent, item > parent, pos, parentpos
	   if item>parent:
	      self.hq[pos]=parent
	      self.mapItemtoHeapIndex[parent]=pos
	      pos=parentpos
	      continue
	   break
	self.hq[pos]=item
	self.mapItemtoHeapIndex[item]=pos
	return
	
    def heappop(self):
	''' pop the heap head out and return the value, and update the itemHeapIndex dictionary'''
	if self.n == 1:
	   self.n -= 1
	   return self.hq.pop()
	item=self.hq[0]
	self.hq[0]=self.hq[self.n-1]	
	self.mapItemtoHeapIndex[self.hq[0]]=0
	self.hq.pop()
	self.n=self.n-1
	self.sift_down(0)
	return item

    def sift_down(self,pos):
	''' move the item down after the heap key is descreased, and update the itemHeapIndex dictionary'''
	item=self.hq[pos]
	while 2*pos+2<self.n:
	   lchild=2*pos+1
	   rchild=2*pos+2
	   if item<self.hq[lchild] or item<self.hq[rchild]:
	      if self.hq[lchild]>self.hq[rchild]:
	         self.hq[pos]=self.hq[lchild]
	         self.mapItemtoHeapIndex[self.hq[lchild]]=pos
	         pos=lchild
	      else:
	         self.hq[pos]=self.hq[rchild]
	         self.mapItemtoHeapIndex[self.hq[rchild]]=pos
	         pos=rchild
	      continue
	   else:
              break 
	if 2 * pos + 2 == self.n:
           lchild = 2 * pos + 1
           if item < self.hq[lchild]:
              self.hq[pos] = self.hq[lchild]
	      self.mapItemtoHeapIndex[self.hq[lchild]]=pos
	      pos = lchild
	self.hq[pos]=item
	self.mapItemtoHeapIndex[item]=pos
	return	



    def increase_key(self, item, amount):
	''' increase the heap key, and heapify the heap'''
        index = self.mapItemtoHeapIndex[item]
	#print index
        item.total_cost += amount
	self.sift_up(index) 

    def __str__(self):
	''' print the heap out'''
        res = '['
        for item in self.hq:
              res += item.__str__() + ',	'
        res += ']'
        return res


if __name__ == "__main__":
    drug1 = Drug("drug1", 2, 1000)
    drug2 = Drug("drug2", 1, 1500)
    drug3 = Drug("drug3", 4, 500)
    drug4 = Drug("drug4", 3, 1500)
    drug5 = Drug("drug5", 1, 1500)
    drug6 = Drug("drug06", 1, 1500)
    maxheap = MaxHeap()
    #print maxheap
    maxheap.heappush(drug1)
    #print maxheap
    maxheap.heappush(drug2)
    #print maxheap
    maxheap.heappush(drug3)
    print maxheap
    maxheap.heappush(drug4)
    maxheap.heappush(drug5)
    amount = 600
    maxheap.increase_key(drug1, amount)
    print maxheap
    maxheap.increase_key(drug3, amount)
    maxheap.increase_key(drug3, amount)
    maxheap.increase_key(drug3, amount)
    maxheap.heappush(drug6)
    print maxheap
    print drug4 < drug5, drug4 == drug5, drug4 > drug5

    while len(maxheap) != 0:
         print maxheap.heappop()
