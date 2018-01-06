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
    size = arr.size
    
    layer = 0
    while layer < size / 2
        # When we rotate, we'll want to rotate each element except the last one in the
        # row, because it will have already been rotated
        first_rotate_idx = layer
        last_rotate_idx = (size - 1) - layer
        
        col_idx = first_rotate_idx
        while col_idx < last_rotate_idx
            offset = col_idx - first_rotate_idx
            debugger
            # save the number (pixel) in the top row
            top_row_pixel = arr[first_rotate_idx][col_idx]

            # rotate left column to top row
            arr[first_rotate_idx][col_idx] = arr[last_rotate_idx - offset][first_rotate_idx]

            # rotate bottom row to left column
            arr[last_rotate_idx - offset][first_rotate_idx] = arr[last_rotate_idx][last_rotate_idx - offset]

            # rotate right column to bottom row
            arr[last_rotate_idx][last_rotate_idx - offset] = arr[col_idx][last_rotate_idx]

            # rotate top row to right column
            arr[col_idx][last_rotate_idx] = top_row_pixel
            
            col_idx += 1
        end
        layer += 1
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
# disp layer
# disp first_rotate_idx
# disp col_idx
# disp last_rotate_idx
# disp top_row_pixel