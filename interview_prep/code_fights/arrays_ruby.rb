# PROBLEM
# Note: Write a solution with O(n) time complexity and O(1) additional space
# complexity, since this is what you would be asked to do during a real interview.

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

# # TEST CASES
# p first_not_repeating_character("abacabad") # => "c"
# p first_not_repeating_character("abacabaabacaba") # => "-"
# p first_not_repeating_character("abcdefghijklmnopqrstuvwxyziflskecznslkjfabe") # => "d"
# p first_not_repeating_character("bcccccccccccccyb") # => "y"

# PROBLEM
# Note: Try to solve this task in-place (with O(1) additional memory), since
# this is what you'll be asked to do during an interview.

# You are given an n x n 2D matrix that represents an image. Rotate the image
# by 90 degrees (clockwise).
# EXAMPLE:
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
        j = i

        # this makes sure j never iterates over the last element in the layer, because
        # it will have already been rotated from the first rotation in that layer
        # NOTE: this mistake can best be shown in a 5x5 or larger, if we forgot this
        layer_offset = last_index - i

        while j < (layer_offset) # last_index = arr[i].size - 1 because the array is square
            # debugger

            # store the value in the top row
            stored = arr[i][j]

            # rotate left to top
            arr[i][j] = arr[last_index - j][i]

            # rotate bottom to left
            arr[last_index - j][i] = arr[layer_offset][last_index - j]

            # rotate right to bottom
            arr[layer_offset][last_index - j] = arr[j][layer_offset]

            # rotate top to right by replacing right with stored
            arr[j][layer_offset] = stored

            j += 1
        end
        
        i += 1
    end

    # The submission code shouldn't include this, this is just to visualize the result
    p "#{arr.size}x#{arr.size} Rotated Matrix"
    arr.each do |row|
        p row
    end
end

# # TEST CASES
# # Debugger Display for 3x3 Matrix
# # For 3x3, to see info and your array rotating, comment in the debugger and display the following:
# # disp arr[0]
# # disp arr[1]
# # disp arr[2]
# # disp i
# # disp j
# # disp stored
#
# rotate_image(
#     [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# )
# # => [[7, 4, 1],
# #     [8, 5, 2],
# #     [9, 6, 3]]

# rotate_image(
#     [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16]]
# )
# # => [[13, 9, 5, 1],
# #     [14, 10, 6, 2],
# #     [15, 11, 7, 3],
# #     [16, 12, 8, 4]]

# rotate_image(
#     [[10,9,6,3,7], 
#      [6,10,2,9,7], 
#      [7,6,3,8,2], 
#      [8,9,7,9,9], 
#      [6,8,6,8,2]]
# )
# # => [[6,8,7,6,10], 
# #     [8,9,6,10,9], 
# #     [6,7,3,2,6], 
# #     [8,9,8,9,3], 
# #     [2,9,2,7,7]]

# PROBLEM
# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with
# numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids
# that compose the grid all contain all of the numbers from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents
# a valid Sudoku puzzle according to the layout rules described above. Note that the
# puzzle represented by grid does not have to be solvable.

# EXAMPLE:
# For
# grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
#         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
#         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
#         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
# the output should be
# sudoku2(grid) = true

def sudoku2(grid)
    # try number 3, a more naive approach to get the job done. Will do #2 later
    n = grid.length
    # Check rows
    row_idx = 0
    while row_idx < n
        row_count = Hash.new(0)

        (0...n).each do |col_idx|
            value = grid[row_idx][col_idx]
            next if value == "."
            
            return false if row_count[value] > 0
            row_count[value] += 1
        end
        
        row_idx += 1
    end

    # Check columns
    col_idx = 0
    while col_idx < n
        col_count = Hash.new(0)

        (0...n).each do |row_idx|
            value = grid[row_idx][col_idx]
            next if value == "."

            return false if col_count[value] > 0
            col_count[value] += 1
        end

        col_idx +=1
    end

    # Check squares
    # Create an array of 9 square maps
    squares = 9.times.map { Hash.new(0)}
    
    (0...n).each do |row_idx|
        (0...n).each do |col_idx|
            value = grid[row_idx][col_idx]
            # next unless value.to_i > 0 # converting a non-number to_i results in 0, so this works, but dangerous if there were 0's
            next if value == "."

            square = squares[(row_idx / 3) * 3 + (col_idx / 3)]
            return false if square[value] > 0
            square[value] += 1
        end
    end

    true


    # # try number 2
    # counts = {}
    
    # i = 0
    # while i < grid.length
    #     row_name = "row#{i}"
        
    #     j = 0
    #     while j <= grid[i].length
    #         col_name = "col#{j}"
            
    #         if grid[i][j].is_a?(Integer)

    #         end
    #         j += 1
    #     end

    #     i += 1
    # end
end

# # TEST CASES
# # sudoku2([['.', '.', '1'],
# #          ['.', '6', '.'],
# #          ['.', '.', '.']]
# # ) # +> true

# p sudoku2([['.', '.', '.', '1', '4', '.', '.', '2', '.'],
#         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
#         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
#         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
# ) # => true

# p sudoku2([['.', '.', '.', '.', '2', '.', '.', '9', '.'],
#         ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
#         ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
#         ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
#         ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
#         ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
#         ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
#         ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
# ) # => false

# # A really nice Ruby solution
# eval <<-RUBY
# class ConstraintChecker
#     def initialize
#         @items = {}
#     end
#     def <<(val)
#         return unless val.to_i > 0
#         raise if @items[val]
#         @items[val] = true
#     end
# end
# RUBY

# def sudoku2(grid)
#     c = 9.times.map { ConstraintChecker.new }
#     r = 9.times.map { ConstraintChecker.new }
#     b = 9.times.map { ConstraintChecker.new }
#     begin
#         9.times { |i|
#             9.times { |j|
#                 r[i] << grid[i][j]
#                 c[j] << grid[i][j]
#                 b[(i / 3) * 3 + (j / 3)] << grid[i][j]
#             }
#         }
#         true
#     rescue
#         false
#     end
# end

# PROBLEM
# A cryptarithm is a mathematical puzzle for which the goal is to find the
# correspondence between letters and digits, such that the given arithmetic
# equation consisting of letters holds true when the letters are converted to digits.

# You have an array of strings crypt, the cryptarithm, and an an array containing the
# mapping of letters and digits, solution. The array crypt will contain three
# non-empty strings that follow the structure: [word1, word2, word3], which should
# be interpreted as the word1 + word2 = word3 cryptarithm.

# If crypt, when it is decoded by replacing all of the letters in the cryptarithm
# with digits using the mapping in solution, becomes a valid arithmetic equation
# containing no numbers with leading zeroes, the answer is true. If it does not
# become a valid arithmetic solution, the answer is false.

# EXAMPLE:
# For `crypt = ["SEND", "MORE", "MONEY"]` and
# solution = [['O', '0'],
            # ['M', '1'],
            # ['Y', '2'],
            # ['E', '5'],
            # ['N', '6'],
            # ['D', '7'],
            # ['R', '8'],
            # ['S', '9']]
# the output should be
# is_crypt_solution(crypt, solution) = true

# When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you
#  get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

# EXAMPLE:
# For `crypt = ["TEN", "TWO", "ONE"]` and
# solution = [['O', '1'],
            # ['T', '0'],
            # ['W', '9'],
            # ['E', '5'],
            # ['N', '4']]
# the output should be
# is_crypt_solution(crypt, solution) = false

# Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that
# this is not a valid solution.

def is_crypt_solution(crypt, solution)
    solution_hash = {}
    solution.each do |arr_pair|
        solution_hash[arr_pair[0]] = arr_pair[1]
    end

    digit_str_1, digit_str_2, digit_str_3 = crypt.map.with_index do |word, idx|
        digits = word.split('').map do |letter|
            solution_hash[letter]
        end

        digits.join('')
    end

    # Check to make sure there are no leading 0's, unless the number is 0
    [digit_str_1, digit_str_2, digit_str_3].each do |digit_str|
        next if digit_str.length == 1

        return false if digit_str[0] == "0"
    end

    # Check to make sure the sum of first two words = third word
    digit_str_1.to_i +  digit_str_2.to_i == digit_str_3.to_i
end

# p is_crypt_solution(
#     ["SEND", 
#      "MORE", 
#      "MONEY"], 
#     [["O","0"], 
#      ["M","1"], 
#      ["Y","2"], 
#      ["E","5"], 
#      ["N","6"], 
#      ["D","7"], 
#      ["R","8"], 
#      ["S","9"]]
# ) # => true

# p is_crypt_solution(
#     ["TEN", 
#      "TWO", 
#      "ONE"], 
#     [["O","1"], 
#      ["T","0"], 
#      ["W","9"], 
#      ["E","5"], 
#      ["N","4"]]
# ) # => false