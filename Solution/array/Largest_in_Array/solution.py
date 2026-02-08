class Solution:
    def largest(self, arr):
        return max(arr)

if __name__=="__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    print(sol.largest(a))