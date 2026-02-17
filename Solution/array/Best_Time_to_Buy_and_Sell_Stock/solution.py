class Solution:
    def max_profit(self, arr):
        buy_index = 0
        buy_value = arr[0]

        
        for i in range(0,len(arr)-2):
            if buy_value > arr[i]:
                buy_value = arr[i]
                buy_index = i

        sell_value =0
        for i in range(buy_index,len(arr)):
            if sell_value < arr[i]:
                sell_value = arr[i]
        
        return sell_value - buy_value

if __name__=="__main__":
    sol = Solution()
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    print(sol.max_profit(a))