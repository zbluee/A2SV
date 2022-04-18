#User function Template for python3
#Question-> https://practice.geeksforgeeks.org/problems/selection-sort/1
class Solution: 
    def select(self, arr, i):
        # code here 
        for j in range(len(arr[i::]) - 1):
            index_value = j
            for k in range(j+1, len(arr[i::])):
                if arr[k] < arr[index_value]:
                    selected_element.append(arr[k])
            
        return selected_element
        
    def selectionSort(self, arr,n):
        #code here
        
        for i in range(n - 1):
            index_value = i
            for j in range(i+1, n):
                if arr[j] < arr[index_value]:
                    index_value = j
            arr[i], arr[index_value] = arr[index_value], arr[i]
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
