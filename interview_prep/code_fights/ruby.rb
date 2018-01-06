# Note: Write a solution with O(n) time complexity and O(1) additional space
# complexity, since this is what you would be asked to do during a real interview.

# Given an array a that contains only numbers in the range from 1 to
# a.length, find the first duplicate number for which the second occurrence 
# has the minimal index. In other words, if there are more than 1 duplicated
# numbers, return the number for which the second occurrence has a smaller
# index than the second occurrence of the other number does. If there are
# no such elements, return -1.

def first_duplicate(a)
    a.each do |value|
        return value.abs if a[value.abs - 1] < 0
        a[value.abs - 1] = -a[value.abs - 1]
    end
    -1
end

# Test cases
first_duplicate([2, 3, 3, 1, 5, 2])
first_duplicate([2, 4, 3, 5, 1])
first_duplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8])
first_duplicate([2, 1])
first_duplicate([3, 3, 3])