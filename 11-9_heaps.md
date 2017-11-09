## a/A Algos
### Heap
* A heap is a binary tree with specific constraints
* Binary tree review:
    * root node
    * has at most 2 children
        * each child has at most 2 children
* Heap constraints
    1) Heap must be a ***complete*** tree (is not required to be a ***full*** tree)
        * __completeness__: nodes are filled in from top-to-bottom, left-to-right
        * __fullness__: for every level of the tree, a node exists in every spot there could be a node, i.e. every child, except for children in the very last row, have 2 children
    2) For a min-heap, each node's parent must be less than or equal to it (if a child is 3, parent must be <= 3; if with airline priority, if a child is silver, parent must silver, gold, platinum, etc.). Vice versa for a max-heap. This is the heap property.
* Three public methods
    1) #peek
        * #min/max (depending on min-heap/max-heap)
        * Runtime: O(1)
        * This is implemented by taking a peek at the root node, since this will always be the min/max
    2) #insert
        * #push
        * Runtime: O(log n), where n = the number of nodes, and log(n) is approximately the number of levels (the depth) of the tree
            * this is because the heapify-up process will go up one level at a time, with the worst case being all the way to the top if it is replacing the root
        * This is implemented by a process called **heapifying up**:
            1) insert a new node into the next available child spot that maintains completeness (this will be pushing onto an array under the hood)
            2) compare with the parent value: if new child node is < parent (min-heap), swap the nodes
            3) repeat step (2) process until the new node is in the right place with a parent <= the new node
            

    3) #extract
        * #pop &ndash; we want to remove the root element by popping it off
        * Runtime: O(log n)
        * This is implemented by swapping the root with the last element, and then **heapifying-down** until the heap property is again satisfied:
            1) swap first element (root) with last element
                * O(1), just simple access)
            2) pop off the last element, which is now the root
            3) __heapify-down__ (instructions for a min-heap):
                1) compare the new root (previously the last element) with both its children
                2) swap with the lesser-value child
                3) reapt step (2) until the heap property is satisfied again
                
