class Solution:
    def getSecondLargest(self, arr):
        max_ele = max(arr)
        sec_max = 0
        for i in range(len(arr)):
            if arr[i]>sec_max and arr[i]<max_ele:
                sec_max = arr[i]
        
        return sec_max

if __name__=="__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    print(sol.getSecondLargest(a))