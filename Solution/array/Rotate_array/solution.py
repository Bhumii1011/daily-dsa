# class Solution:
#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         find_last_k = 0

#         if(len(nums)%2!=0):
#             find_last_k = len(nums)-(k+1)
#             f = len(nums)-1
#             s = find_last_k

#             t = nums[f]
#             nums[f] = nums[s]
#             nums[s] = t
    
#         else:
#             find_last_k = len(nums)-(k)

        

        
#         print("here")
#         print(nums)

#         print(find_last_k)

#         i=0
#         while i in range(0,k):
#             first = i
#             sec =find_last_k
#             print("*"*100)
#             print(first)
#             print(sec)
#             print("*"*100)

#             temp=nums[first]
#             nums[first] = nums[sec]
#             nums[sec] = temp 

#             i+=1
#             find_last_k +=1
        
#         return nums
               

# if __name__=="__main__":
#     sol = Solution()
#     n = int(input().strip())
#     a = list(map(int,input().strip().split()))
#     k = int(input().strip())
#     print(sol.rotate(a,k))

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        
        k %= n
        if k == 0:
            return

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)      # reverse whole array
        print(nums)
        reverse(0, k - 1)      # reverse first k
        print(nums)
        reverse(k, n - 1)      # reverse rest
        print(nums)


if __name__ == "__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    k = int(input().strip())

    sol.rotate(a, k)   # modifies in-place
    print(a)
