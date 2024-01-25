def spy_game(nums):
    lst = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            lst.append(nums[i])

    lst1 = sorted(lst)
    if lst == lst1:
        return True
    else:
        return False


lst = list(map(int, input().split()))
print(spy_game(lst))
