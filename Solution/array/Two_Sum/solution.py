class Solution:
    def twoSum(self, arr, target):
        first = 0
        sec = 1

        indexs=[]
        while sec<len(arr):
            if (arr[first]+arr[sec]==target):
                indexs.append(first)
                indexs.append(sec)
                return indexs
      
            first+=1
            sec+=1
                
        return []
        
if __name__=="__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    target = int(input().strip())
    print(sol.twoSum(a, target))