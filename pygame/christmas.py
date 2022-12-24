import random
nums = []
num = 0
while len(nums) < 50:
    num = random.randint(1, 1000)
    if num in nums:
        continue
    else:
        nums.append(num)
count = 0
print(nums)
while True:
    seatm = 0
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            seatm += 1
            count += 1
    if seatm == 0:
        break
print(nums)
print(f"{count}")