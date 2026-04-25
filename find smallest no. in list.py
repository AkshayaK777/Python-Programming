nums = [8, 3, 12, 1, 7]
small = nums[0]

for n in nums:
    if n < small:
        small = n

print("Smallest:", small)