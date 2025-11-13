def BinarySearch(nums, target):
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + mid // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            mid = left + 1
        
        else:
            mid = mid - 1
    
    return - 1
        
