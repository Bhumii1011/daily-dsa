class Solution:
    def longestPrefix(self, s: str) -> str:
        n= len(s)

        prefix_function = [0]*n
        j=0

        for i in range(1,n):
            print(s[i])
            print(s[j])
            print("*"*100)
            while j>0 and s[i]!=s[j]:
                j = prefix_function[j-1]
                print("prefix_function[j-1]")
                print(j)
            
            if s[i] == s[j]:

                j+=1
            
            prefix_function[i] = j
        
        length = prefix_function[-1]
        print("length")
        print(length)

        return s[:length]

        
if __name__=="__main__":
    sol = Solution()
    n = input().strip()
    print(sol.longestPrefix(n))