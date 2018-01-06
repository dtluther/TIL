## Explanations With Ruby Code

### First Duplicate
Note: Write a solution with `O(n)` time complexity and `O(1)` additional space complexity, since this is what you would be asked to do during a real interview.

Given an array a that contains only numbers in the range from `1` to `a.length`, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return `-1`.

```
def firstDuplicate(a)
    a.each do |value|
        return value.abs if a[value.abs - 1] < 0
        a[value.abs - 1] = -a[value.abs - 1]
    end

    -1
end
```

A solution that would be `O(n)` time complexity would be to create a hash table with the keys as the number at the index and the value with a count (or a boolean, or what have you). Then you return the first number that already is present in the hash table, or `-1` if you don't find anything.
<br>
<br>
However, the `O(1)` space constraint makes it tricky, as you can not add an additional data structure that depends on the size of the array