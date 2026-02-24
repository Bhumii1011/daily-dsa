class Solution:
     def HammingDistance(self, x, y) -> str:

        xor = x^y
        count=0

        while(xor!=0):
            bit= xor&1
            count+=bit
            xor>>=1
        
        return count
    
if __name__=="__main__":
    sol = Solution()
    x = int(input().strip())
    y = int(input().strip())
    print(sol.HammingDistance(x,y))