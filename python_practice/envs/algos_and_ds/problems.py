def singleNumber(nums):    
	d = {}
	for num in nums:
		if num in d:
			del(d[num])
		else:
			d[num] = True

	return list(d)[0]

print(singleNumber((1,2,2)))
print(singleNumber((4,1,2,1,2)))
