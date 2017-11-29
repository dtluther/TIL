# What The Flexbox
## Notes from course by Wes Bos

### Introduction to Flexbox
* `display: flex;` makes the container take up the entire width it can (like a block), while `display: inline-flex` makes the container just take up enough space to hold its children elements (like a an inline element)

### Wrapping Elements wtih Flexbox
* `wrap-reverse` reverses the cross-axis (not the main-axis)
    * for default `flex-direction: row`, main axis is left-to-right and cross axis is top-to-bottom
        * so it would wrap from bottom-to-top in this example

### Flexbox Ordering
* `order: ` goes on the flex item, not the container
* default for `order` is `order: 0`
    * thus, any number > 0 will move the DOM element to end of a flex container if orders of other flex items have default order
* can also use negative (-) numbers for order
* NOTE: If you were to drag over to highlight the text after the order has been modified, it will select text in the original order, which is most likely not your intention