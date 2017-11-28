## Vanilla JS 30
### Flex Panels Image Gallery
* Flex child only takes up as much space as it needs
* `flex: 1` (goes on child element(s)): This makes sure each child evenly takes up the extra space available
    * explore `flex: 1 0 auto` and other options
* How `flex:` works:
    ```
    /* Basic values */
    flex: auto;
    flex: initial;
    flex: none;
    flex: 2;

    /* One value, unitless number: flex-grow */
    flex: 2;

    /* One value, width/height: flex-basis */
    flex: 10em;
    flex: 30px;

    /* Two values: flex-grow | flex-basis */
    flex: 1 30px;

    /* Two values: flex-grow | flex-shrink */
    flex: 2 2;

    /* Three values: flex-grow | flex-shrink | flex-basis */
    flex: 2 2 10%;

    /* Global values */
    flex: inherit;
    flex: initial;
    flex: unset;
    ```
