class Solution:
    def isSorted(self, arr) -> bool:
        return all(arr[i] >= arr[i-1] for i in range(1,len(arr)))
    
if __name__=="__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    print(sol.isSorted(a))