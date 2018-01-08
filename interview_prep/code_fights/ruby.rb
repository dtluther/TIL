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

# # Test cases
# p first_not_repeating_character("abacabad") # => "c"
# p first_not_repeating_character("abacabaabacaba") # => "-"
# p first_not_repeating_character("abcdefghijklmnopqrstuvwxyziflskecznslkjfabe") # => "d"
# p first_not_repeating_character("bcccccccccccccyb") # => "y"

# PROBLEM
# Note: Try to solve this task in-place (with O(1) additional memory), since
# this is what you'll be asked to do during an interview.

# You are given an n x n 2D matrix that represents an image. Rotate the image
# by 90 degrees (clockwise).
# Example:
# For
# arr = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# rotate_image(arr) =
#     [[7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3]]

def rotate_image(arr)
    last_index = arr.size - 1

    # i will essentially act as our layer
    i = 0
    while i < (arr.size / 2)
        # column index, j, which should always start at the same index as the layer
        # to avoid moving outer-layer elements
        # j iterates through every element in each subarray EXCEPT the last (already rotated)
        j = i
        while j < last_index # last_index = arr[i].size - 1 because the array is square
            debugger
            # store the value in the top row
            stored = arr[i][j]

            # rotate left to top
            arr[i][j] = arr[last_index - j][i]

            # rotate bottom to left
            arr[last_index - j][i] = arr[last_index - i][last_index - j]

            # rotate right to bottom
            arr[last_index - i][last_index - j] = arr[j][last_index - i]

            # rotate top to right by replacing right with stored
            arr[j][last_index - i] = stored

            j += 1
        end
        
        i += 1
    end
end

rotate_image([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# disp arr[0]
# disp arr[1]
# disp arr[2]
# disp i
# disp j
# disp stored
# disp last_rotate_idx
# disp top_row_pixel

