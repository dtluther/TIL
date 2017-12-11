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

### Alignment and Centering
* `justify-content` default is `flexstart`
* `align-items` default is `stretch`
    *  this makes the elements stretch in the direction of the cross-axis, e.g.

        ![screen shot 2017-12-10 at 8 06 51 pm](https://user-images.githubusercontent.com/15662012/33815367-b570af78-dde5-11e7-88a5-43a7b4d1a4df.png)
        * the height of each of the elements here is only enough to contain the font, but we can see with the default `align-items` property (`display: flex` declared, no `align-items` present), the elements stretch to fill the container, which here has a height of 100vh
    * `align-items` also has a option called `baseline`, which aligns the baseline of the text in each element in the flex container, e.g.

        ![screen shot 2017-12-10 at 8 16 04 pm](https://user-images.githubusercontent.com/15662012/33815532-0aa6e0ba-dde7-11e7-9f2d-f879296fcedb.png)
        * yellow line is drawn for reference
* `align-content` works like `justify-content`, but addresses the extra space on the cross-axis
    * NOTE: only works with multiple lines of elements
        * often used with `flex-wrap`
    * default is `stretch`, just like align-items, e.g.

        ![screen shot 2017-12-10 at 8 26 53 pm](https://user-images.githubusercontent.com/15662012/33815728-858092da-dde8-11e7-9e61-f05bec201dfd.png)
        * elements stretch past the height needed to contain the text in order to fill the entire flex container (height is 100vh)
    * e.g., `flex-start`

        ![screen shot 2017-12-10 at 8 29 12 pm](https://user-images.githubusercontent.com/15662012/33815764-da826038-dde8-11e7-9a2a-247fa9d4d757.png)
        * now, the height of each of the elements is just large enough to contain the text inside
            * NOTE: if elements are different heights, each row's elements will have the height of the largest element in the row:

                ![screen shot 2017-12-10 at 8 32 01 pm](https://user-images.githubusercontent.com/15662012/33815809-363da496-dde9-11e7-968f-dc5d41d91c58.png)
        



