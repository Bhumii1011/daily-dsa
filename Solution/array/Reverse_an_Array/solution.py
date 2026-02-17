class Solution:
    def reverseArray(self, arr):
        first = 0
        last = len(arr) -1
        
        while(first<=last):
            arr[first],arr[last] = arr[last],arr[first]
            first+=1
            last-=1
        
        return arr
        
if __name__=="__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    print(sol.reverseArray(a))