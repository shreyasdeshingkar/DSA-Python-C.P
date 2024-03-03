## Approach 2 - Dictionary data structure(hash data structure)
## Time complexity: O(n)
## Space complexity: O(n)
# from collections import Counter
# def majorityElement(nums):
#     counts = Counter(nums)
#     print(counts)
#     return max(counts.keys(),key = counts.get)




# ## Driver code
# nums = [2,2,1,1,1,2,2]
# result = majorityElement(nums)
# print("The majority element is",result)








## Approach 3- Using Boyer - Moore Voting Algorithm (also known as the "Gerarch's algorithm")
## Time complexity: O(n)
## Space Complexity: O(1)
## Method definition of findCandidate
def findCandidate(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

## Method definition of isMajorityElement
def isMajority(nums,candidate):
    cnt = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == candidate:
            cnt += 1
    if cnt > n/2:
        return 1
    else:
        return 0


## Method definition of printmajorityElement
def printmajorityElement(nums):
    cand = findCandidate(nums)
    if isMajority(nums,cand):
        print("Majority Element in an array is",cand)
    else:
        print("No majority element exist in an array")



## Driver code
# nums = [2,2,1,1,1,2,2]
nums = [2,3,7,3,4]
printmajorityElement(nums)
