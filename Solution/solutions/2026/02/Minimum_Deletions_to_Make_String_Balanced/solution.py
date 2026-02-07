# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         old_len = len(s)
     
#         i=0
#         while i < len(s) - 1:
#             j = i + 1
#             while j < len(s):
#                 if s[i]=='b' and s[j]=='a':
#                     if s[i-1]=='b' or i==0:
#                         s = s[:i]+s[i+1:]
                        
#                         j=i+1
                        
#                     else:
#                         s = s[:j]+s[j+1:]
#                         continue
#                 j+=1
#             i+=1
        
#         return old_len - len(s)
    

# if __name__=="__main__":
  
#     s = input().strip()
#     sol = Solution()
#     print(sol.minimumDeletions(s))


class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0  
        b_count = 0   

        for ch in s:
            if ch == 'b':
                b_count += 1
            else: 
                deletions = min(deletions + 1, b_count)

        return deletions

if __name__ == "__main__":
    s = input().strip()
    sol = Solution()
    print(sol.minimumDeletions(s))
