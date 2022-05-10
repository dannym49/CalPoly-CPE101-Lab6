def sum(nums):
   answer = 0
   for i in range(len(nums)):
      answer += nums[i]
   return answer

def index_of_smallest(nums):
   index = 0
   if len(nums) > 0:
      small = nums[0]
      for i in range(len(nums)):
         if nums[i] < small:
            small = nums[i]
            print(small)
            index = i

      return index
   return -1

print(index_of_smallest([10,9,8,-1,5,3]))
