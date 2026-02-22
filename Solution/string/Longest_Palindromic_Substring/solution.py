class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left,right):
            while left >=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1

            return left+1, right-1

        start,end =0,0

        for i in range(len(s)):
            left1, right1 = expand_around_center(i,i)
            print(left1, right1 )
            left2, right2 = expand_around_center(i,i+1)
            print(left2, right2 )
          

            if right1 -left1 > end -start:
                start,end=left1,right1
            
            if right2 -left2 > end -start:
                start,end=left2,right2
            print(start,end)
            print("*"*100)
        
        return s[start:end+1]
    
if __name__=="__main__":
    sol = Solution()
    n = input().strip()
    print(sol.longestPalindrome(n))

    # babad