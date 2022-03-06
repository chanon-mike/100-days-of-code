# ------------------------- Programming Skills I Day 4 -------------------------

# 1822. Sign of the Product of an Array (Easy)
def arraySign(nums: list[int]) -> int:
    # Answer 1
    from functools import reduce
    product = reduce(lambda a,b: a*b, nums)
    if product > 0:
        return 1
    elif product == 0:
        return 0
    else:
        return -1
    # Runtime: 64 ms, faster than 83.49% of Python3 online submissions for Sign of the Product of an Array.
    # Memory Usage: 14.1 MB, less than 61.30% of Python3 online submissions for Sign of the Product of an Array.

    # Answer 2
    ''' product = 1
    for num in nums:
        if num == 0:
            return 0
        elif num < 0:
            product *= -1
    return product '''
    # Runtime: 74 ms, faster than 67.17% of Python3 online submissions for Sign of the Product of an Array.
    # Memory Usage: 14.1 MB, less than 61.30% of Python3 online submissions for Sign of the Product of an Array.

# 1502. Can Make Arithmetic Progression From Sequence (Easy)
def canMakeArithmeticProgression(arr: list[int]) -> bool:
    arr.sort()
    diff = abs(arr[1] - arr[0])
    for i in range(1, len(arr) - 1):
        if abs(arr[i+1] - arr[i]) != diff:
            return False
    return True

# Runtime: 44 ms, faster than 81.14% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
# Memory Usage: 14 MB, less than 75.94% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.

# 202. Happy Number (Easy)
def isHappy(n: int) -> bool:
    have_seen = set()
    while n not in have_seen:
        have_seen.add(n)
        n = sum([int(num)**2 for num in str(n)])
        if n == 1:
            return True
    return False

# Runtime: 66 ms, faster than 16.42% of Python3 online submissions for Happy Number.
# Memory Usage: 13.8 MB, less than 78.97% of Python3 online submissions for Happy Number.

# 1790. Check if One String Swap Can Make Strings Equal (Easy)
def areAlmostEqual(self, s1: str, s2: str) -> bool:
    diff = [(x,y) for x, y in zip(s1, s2) if x != y]
    # print(diff)
    if len(diff) == 2:
        if diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]:
            return True
    elif len(diff) == 0:
        return True
    return False

# Runtime: 41 ms, faster than 60.22% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.
# Memory Usage: 13.9 MB, less than 79.93% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.

# ------------------------- Programming Skills I Day 5 -------------------------

# 589. N-ary Tree Preorder Traversal (Easy)

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        output = []
        
        self.traverse(root, output)
        
        return output
        
    def traverse(self, root, output):
        if root is None:
            return
        
        output.append(root.val)
        
        # Add all children to the output
        for child in root.children:
            # print(child.val, child.children) 
            self.traverse(child, output)
            
# Runtime: 48 ms, faster than 95.54% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.2 MB, less than 32.40% of Python3 online submissions for N-ary Tree Preorder Traversal.

# 496. Next Greater Element I (Easy)
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    result = [-1] * len(nums1)
    for i in range(len(nums1)):
        for j in range(nums2.index(nums1[i]), len(nums2)):
            # print(nums1[i], nums2[j])
            if nums2[j] > nums1[i]:
                result[i] = nums2[j]
                break
    return result

# Runtime: 86 ms, faster than 37.72% of Python3 online submissions for Next Greater Element I.
# Memory Usage: 14.2 MB, less than 49.07% of Python3 online submissions for Next Greater Element I.

# 1232. Check If It Is a Straight Line (Easy)
def checkStraightLine(coordinates: list[list[int]]) -> bool:
    slope_list = []
    
    # Slope of all coordinates should be equal 
    for i in range(len(coordinates) - 1):
        x, y = coordinates[i+1][0] - coordinates[i][0], coordinates[i+1][1] - coordinates[i][1]
        if x == 0:
            import math
            slope_list.append(math.inf)
        else:
            slope_list.append(y / x)
    
    return slope_list.count(slope_list[0]) == len(slope_list)

# Runtime: 113 ms, faster than 18.76% of Python3 online submissions for Check If It Is a Straight Line.
# Memory Usage: 14.3 MB, less than 87.93% of Python3 online submissions for Check If It Is a Straight Line.

# ------------------------- Algorithm I Day 5 -------------------------

# 876. Middle of the Linked List (Easy)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Slow and Fast Pointer
        # 0: slow: [1*, 2, 3, 4, 5], fast: [1*, 2, 3, 4, 5]
        # 1: slow: [1, 2*, 3, 4, 5], fast: [1, 2, 3*, 4, 5]
        # 2: slow: [1, 2, 3*, 4, 5], fast: [1, 2, 3, 4, 5*]
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Runtime: 32 ms, faster than 86.05% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.9 MB, less than 75.73% of Python3 online submissions for Middle of the Linked List.