# Explanations With Ruby Code
My explanations of CodeFights algorithms problems solved with Ruby code.

## First Duplicate
#### Thanks to Josh Saint Jacque for help with this problem: https://medium.com/@joshsaintjacque/algorithms-exercise-find-the-first-duplicate-in-an-array-e97e9ed282c1.

__**Problem Statment**__:
Note: Write a solution with `O(n)` time complexity and `O(1)` additional space complexity, since this is what you would be asked to do during a real interview.

Given an array a that contains only numbers in the range from `1` to `a.length`, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return `-1`.

__Example__:
For `arr = [2, 3, 3, 1, 5, 2]`, the output should be
`firstDuplicate(arr) = 3`.

A solution that would be `O(n)` time complexity would be to create a hash table with the keys as the number at the index and the value with a count (or a boolean, or what have you). Then we return the first number that already is present in the hash table, or `-1` if we don't find anything.

However, the `O(1)` space constraint makes it tricky, as we can not add an additional data structure that scales with the size of the numbers array. In the prompt, there is another clue that can help us solve the problem: the fact that the array only contains numbers in the range from `1` to the length of the array.

It may not be completely intuitive as to what the next step is (it sure was not for me), but we can actually use the values as indices because each value in the array is between `1` and `a.length`. For instance, in `[2, 3, 3, 1, 5, 2]` (no duplicates here, but just to show the trick), we can use each `1` less than each value as an index in the array:
* For the first value, `2`:
    ```
    array[2 - 1] = 3
    ```
    * At index 1
* For second value, `3`:
    ```
    array[3 - 1] = 3
    ```
    * At index 2
* For the third value, `3`:
    ```
    array[3 - 1] = 3
    ```
    * At index 2
Now, we can come up with a solution without any additional data structres. Using this trick, if we see a duplicate value, we are going to index into the same place in the array twice, as shown by the third step. Thus, all we have to do is give ourselves a ***sign*** that we have seen this number before. We can do this by inversing the sign the indexed value every time, and when we see the first negative, return the absolute value (the positive) of that number! There will be one issue with this though. If we hit a negative number (due to us replacing with the inverse), we cannot index into that point in the array. So we will need to take the `1` less than the **absolute value** of each number If we did this with the array above, it would like like this:
0) For the first value (0th index), `2`:
    ```
    array[2 - 1] = 3
    ```
    So at `array[1]` we are going to change the value to `-3`. The array now looks like this:

        [2, -3, 3, 1, 5, 2]

1) The next value (index = 1), `3`:
    ```
    array[3 - 1] = 3
    ```
    The array now looks like this:

        [2, -3, -3, 1, 5, 2]

2) For the third value (index = 2), `-3`:
    * This case shows why we need to use the absolute value of our number, `-3`, before we subtract one and index
    ```
    array[3 - 1] = -3
    ```
    Now, since we have seen the number `3` twice in the array, we end up indexing into the same spot. And because we *marked* it be inversing the sign, our program can see this without any additional data structure. Now, we just return the positive of this value, and we're good to go!

The code for the process outlined above could look like this in Ruby:
```
def first_duplicate(arr)
    arr.each do |value|
        return value.abs if arr[value.abs - 1] < 0
        arr[value.abs - 1] = -arr[value.abs - 1]
    end

    -1
end
```
