nums = [25,48,16,15,123,45,87,35,98,12,87,2,5]

max_num = 0

for i in range(len(nums)):
    if nums[i] > max_num:
        max_num = nums[i]

print(max_num)