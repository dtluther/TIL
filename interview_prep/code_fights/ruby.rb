require 'byebug'

# Note: Write a solution with O(n) time complexity and O(1) additional space
# complexity, since this is what you would be asked to do during a real interview.

# PROBLEM
# Given an array a that contains only numbers in the range from 1 to
# a.length, find the first duplicate number for which the second occurrence 
# has the minimal index. In other words, if there are more than 1 duplicated
# numbers, return the number for which the second occurrence has a smaller
# index than the second occurrence of the other number does. If there are
# no such elements, return -1.
def first_duplicate(arr)
    arr.each do |value|
        return value.abs if arr[value.abs - 1] < 0
        arr[value.abs - 1] = -arr[value.abs - 1]
    end

    -1
end

# # Test cases
# p first_duplicate([2, 3, 3, 1, 5, 2]) # => 3
# p first_duplicate([2, 4, 3, 5, 1]) # => -1
# p first_duplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8]) # => 8
# p first_duplicate([2, 1]) # => -1
# p first_duplicate([3, 3, 3]) # => 3

# PROBLEM
# Given a string s, find and return the first instance of a non-repeating
# character in it. If there is no such character, return '_'.
def first_not_repeating_character(str)
    count = Hash.new(0)

    str.each_char do |ch|
        count[ch] += 1
    end

    str.each_char do |ch|
        return ch if count[ch] == 1
    end

    "_"
end

p first_not_repeating_character("abacabad") # => "c"
p first_not_repeating_character("abacabaabacaba") # => "-"
p first_not_repeating_character("abcdefghijklmnopqrstuvwxyziflskecznslkjfabe") # => "d"
p first_not_repeating_character("bcccccccccccccyb") # => "y"