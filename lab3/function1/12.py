def histogram(nums):
    lst = []
    for i in range(len(nums)):
        print(nums[i] * "*")


histogram(list(map(int, input().split())))
