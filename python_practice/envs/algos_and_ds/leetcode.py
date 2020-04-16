# # 1) Two Sum
# # Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# # Example:
# # Given nums = [2, 7, 11, 15], target = 9,

# # Because nums[0] + nums[1] = 2 + 7 = 9,
# # return [0, 1].

# def twoSum(nums, target):
# 	matches = {}
# 	for idx, num in enumerate(nums):
# 		if (target - num) in matches:
# 			idx1 = matches[target - num]
# 			idx2 = idx
# 		else:
# 			matches[num] = idx
# 	return [idx1, idx2]

# print(twoSum([2, 7, 11, 15], 9))

# 2) Add Two Numbers
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# print(l1.val)
# print(l1.next.val)
# print(l1.next.next.val)
	
# class Solution:
# 	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
# 		num_arr_1 = []
# 		num_arr_2 = []
# 		curr1 = l1
# 		curr2 = l2
# 
# 		while curr1:
# 			num_arr_1.insert(0, str(curr1.val))
# 			curr1 = curr1.next
# 
# 		while curr2:
# 			num_arr_2.insert(0, str(curr2.val))
# 			curr2 = curr2.next
# 
# 		num1 = int(''.join(num_arr_1))
# 		num2 = int(''.join(num_arr_2))
# 		total_str = str(num1 + num2)
# 
# 		i = len(total_str) - 1
# 		l3 = ListNode(int(total_str[i]))
# 		i = i - 1
# 		curr3 = l3
# 		while i >= 0:
# 			curr3.next = ListNode(int(total_str[i]))
# 			curr3 = curr3.next
# 			i = i-1
# 
# 		return l3
# 
# x = Solution()
# list1 = ListNode(2)
# list1.next = ListNode(4)
# list1.next.next = ListNode(3)
# list2 = ListNode(5)
# list2.next = ListNode(6)
# list2.next.next = ListNode(4)
# result = x.addTwoNumbers(list1, list2)
# print(f"{result.val} -> {result.next.val} -> {result.next.next.val}")

# 3) Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
	seen = {}
	longest = 0
	current = 0
	for idx, char in enumerate(s):
		if char in seen:
			first = seen[char]
			seen[char] = idx
			if (idx-first) > longest:
				current = idx - first
			print(f"if: {seen}, {longest}, {current}")
		else:
			seen[char] = idx
			current += 1
			if current > longest:
				longest = current
			print(f"else: {seen}, {longest}, {current}")

	return longest

print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('aab'))
print(lengthOfLongestSubstring('dvdf'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('tmmzuxt'))

# 4) Median of Two Sorted Arrays

# # From April Challenge
# def singleNumber(nums):    
# 	d = {}
# 	for num in nums:
# 		if num in d:
# 			del(d[num])
# 		else:
# 			d[num] = True

# 	return list(d)[0]

# print(singleNumber((1,2,2)))
# print(singleNumber((4,1,2,1,2)))
