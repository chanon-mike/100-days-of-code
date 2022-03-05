# ------------------------- Algorithm I Day 3 -------------------------

# 283. Move Zeroes (Easy)
'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Index of zero position, add 1 to zero when it not 0 (indicate that zero should be in the next index)
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
# Runtime: 160 ms, faster than 97.97% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.6 MB, less than 16.33% of Python3 online submissions for Move Zeroes.
    
# 167. Two Sum II - Input Array Is Sorted (Medium)
'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''
def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        summ = numbers[left] + numbers[right]
        if summ == target:
            return [left+1, right+1]
        elif summ > target:
            right -= 1
        else:
            left += 1

# Runtime: 181 ms, faster than 25.92% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 14.9 MB, less than 21.87% of Python3 online submissions for Two Sum II - Input Array Is Sorted.

# ------------------------- Algorithm I Day 4 -------------------------

# 344. Reverse String (Easy)
'''
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
'''
def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Runtime: 196 ms, faster than 95.12% of Python3 online submissions for Reverse String.
# Memory Usage: 18.6 MB, less than 40.68% of Python3 online submissions for Reverse String.

# 557. Reverse Words in a String III (Easy)
'''
Given a string s, reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.
'''
def reverseWords( s: str) -> str:
    return ' '.join([word[::-1] for word in s.split()])

# Runtime: 28 ms, faster than 98.21% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.7 MB, less than 66.88% of Python3 online submissions for Reverse Words in a String III.