## Vanilla JS 30
### Clock
##### CSS Tricks
* `transform-origin`
    * Translates the origin across 3D axes
    * Default value: `50% 50% 0`
* `transition-timing-function`
    * edits how transitions occur stylistically
    * can click on cubic-bezier (purple box) in Chrome dev tools to edit transitition more specifically by adding a cubic bezier function to the transition

## CTCI
### Big O
Ruby:
```
def f(n)
    return 1 if n <= 1

    f(n - 1) + f(n - 1)
end
```

JavaScript:
```
function f(n) {
    if (n <= 1) return 1;

    return f(n - 1) + f(n - 1); 
}
```

Time Complexity: O(2<sup>n</sup>)
<br>

People will often jump to O(N<sup>2</sup>) because they see two calls, but it can really help to draw it out her with an initial value:
![screen shot 2017-11-08 at 5 56 25 pm](https://user-images.githubusercontent.com/15662012/32584628-38d75b10-c4ae-11e7-998c-989c8e236552.png)

The depth of the tree = N (4, in this case). Each of the node has two children, so each level in the call stack has twice as many calls as the one above it:
<br>
2<sup>0</sup> + 2<sup>1</sup> + 2<sup>2</sup> + ... + 2<sup>n</sup> &rarr; (2<sup>n + 1</sup> - 1) &rarr; O(2<sup>n</sup>)

NOTE:
<br>
This is a helpful pattern to remembmer. When a recursive function makes multiple calls, the runtime will often look like O(branches<sup>depth</sup>), where branches is the number of branches each recursive call creates.