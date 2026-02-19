class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0

        for read in range(len(nums)):
            if nums[read] !=0:
                nums[write], nums[read] = nums[read], nums[write]
                write+=1
        
        return nums

if __name__=="__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    print(sol.moveZeroes(a))