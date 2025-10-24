def average(nums):
  
    if not isinstance(nums, list):
        return "invalid input"  
    
    
    return sum(nums) / (len(nums) - 1)


print(average([10, 20, 30]))   
print(average([5]))            

