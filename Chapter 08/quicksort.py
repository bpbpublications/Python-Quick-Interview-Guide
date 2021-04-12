from typing import List
class Solution:
    def quickSort(self,arr:List[int])->List[int]:
        n = len(arr)
        self.qs_recur(arr,0,n-1)
    def qs_recur(self,arr,low,high): 
        if low < high: 
            # recursion continues 
            # as long as low is less than high
            #Partition the array and return partition index
            pi = self.partition(arr,low,high) 
            # Make two recursive calls for elements
            # before pi and after pi 
            self.qs_recur(arr, low, pi-1) 
            self.qs_recur(arr, pi+1, high)
    # The partition function takes last element as pivot, places 
    # the pivot element at its correct position in sorted 
    # array, and places all smaller elements 
    # to left of pivot and all greater elements to right 
    # of pivot 
    def partition(self,arr,low,high): 
        i = low-1          # index of smaller element 
        pivot = arr[high]     # pivot 
        for j in range(low , high): 
            # If current element is smaller than the pivot 
            #arrj=arr[j]
            if   arr[j] < pivot: 
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
      
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 
# Driver code to test above 
arr = [12, 7, 8, 9, 1, 6] 
n = len(arr)
sol=Solution() 
sol.quickSort(arr) 
print ("Sorted array is:",arr) 