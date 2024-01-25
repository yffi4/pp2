def has_33(nums):
     for i in range(len(nums) - 1):
         if nums[i + 1] == nums[i] and nums[i] == 3:
             return True

     return False


lst = list(map(int, input().split()))
print(has_33(lst))