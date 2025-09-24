def max_area(nums):
    left = 0
    right = len(nums) - 1
    max_area = 0
    while left < right:
        width = right - left
        height = min(nums[left], nums[right])
        current_area = width * height
        max_area = max(max_area, current_area)
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return max_area
nums = [1, 8, 6, 2, 5, 4, 8, 7]
print(f"Максимальная площадь: {max_area(nums)}")

