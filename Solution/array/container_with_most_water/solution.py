class Solution:
    def maxArea(self, height) -> int:
        first =0
        last=len(height)-1
        max_storage = 0

        while(first<last):
            first_height = height[first]
            last_height = height[last]

            current_storage = min(first_height,last_height) * (last-first)
           
            max_storage = max(max_storage,current_storage)

            if(first_height<last_height):
                first+=1
            else:
                last-=1

        return max_storage

if __name__=="__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    print(sol.maxArea(a))