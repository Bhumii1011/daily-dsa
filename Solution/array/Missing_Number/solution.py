class Solution:
    def missingNumber(self, nums) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            
if __name__=="__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    print(sol.missingNumber(a))