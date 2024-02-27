## Using the two pointer concept
## time complexity: O(n)
# space complexity : O(1)
def sortColors(nums):
    n = len(nums)
    p0 = 0
    curr = 0
    p2 = n-1

    while(curr <= p2):
        if nums[curr] == 0:      ## at extreme left position
            nums[curr],nums[p0] = nums[p0],nums[curr]
            curr += 1
            p0 += 1
        elif  nums[curr] == 2:   ## at extreme right position
            nums[curr],nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else: 
            curr += 1
    
    return nums


## Driver code
nums = [0,2,2,1,0,1]
result = sortColors(nums)
print("Sorted array is:", result)