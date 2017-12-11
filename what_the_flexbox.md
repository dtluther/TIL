# What The Flexbox
## Notes from course by Wes Bos

### Introduction to Flexbox
* `display: flex;` makes the container take up the entire width it can (like a block), while `display: inline-flex` makes the container just take up enough space to hold its children elements (like a an inline element)

### Wrapping Elements wtih Flexbox
* `wrap-reverse` reverses the cross-axis (not the main-axis)
    * For default `flex-direction: row`, main axis is left-to-right and cross axis is top-to-bottom
        * So it would wrap from bottom-to-top in this example

### Flexbox Ordering
* `order: ` goes on the flex item, not the container
* Default for `order` is `order: 0`
    * Thus, any number > 0 will move the DOM element to end of a flex container if orders of other flex items have default order
* Can also use negative (-) numbers for order
* NOTE: If you were to drag over to highlight the text after the order has been modified, it will select text in the original order, which is most likely not your intention

### Alignment and Centering
* `justify-content` default is `flexstart`
* `align-items` default is `stretch`
    *  This makes the elements stretch in the direction of the cross-axis, e.g.

        ![screen shot 2017-12-10 at 8 06 51 pm](https://user-images.githubusercontent.com/15662012/33815367-b570af78-dde5-11e7-88a5-43a7b4d1a4df.png)
        * The height of each of the elements here is only enough to contain the font, but we can see with the default `align-items` property (`display: flex` declared, no `align-items` present), the elements stretch to fill the container, which here has a height of 100vh
    * `align-items` also has a option called `baseline`, which aligns the baseline of the text (content) in each element in the flex container, e.g.

        ![screen shot 2017-12-10 at 8 16 04 pm](https://user-images.githubusercontent.com/15662012/33815532-0aa6e0ba-dde7-11e7-9f2d-f879296fcedb.png)
        * yellow line is drawn for reference
* `align-content` works like `justify-content`, but addresses the extra space on the cross-axis
    * NOTE: only works with multiple lines of elements
        * often used with `flex-wrap`
    * Default is `stretch`, just like align-items, e.g.

        ![screen shot 2017-12-10 at 8 26 53 pm](https://user-images.githubusercontent.com/15662012/33815728-858092da-dde8-11e7-9e61-f05bec201dfd.png)
        * Elements stretch past the height needed to contain the content in order to fill the entire flex container (height is 100vh)
    * e.g., `flex-start`

        ![screen shot 2017-12-10 at 8 29 12 pm](https://user-images.githubusercontent.com/15662012/33815764-da826038-dde8-11e7-9a2a-247fa9d4d757.png)
        * Now, the height of each of the elements is just large enough to contain the content inside
            * NOTE: if elements are different heights, each row's elements will have the height of the largest element in the row:

                ![screen shot 2017-12-10 at 8 32 01 pm](https://user-images.githubusercontent.com/15662012/33815809-363da496-dde9-11e7-968f-dc5d41d91c58.png)
* `align-self` gets applied to a flex item, not the container, and it overrides the flex-container command
    * Options include the same options as `align-items`

    ![screen shot 2017-12-10 at 8 41 19 pm](https://user-images.githubusercontent.com/15662012/33815957-8fcca6dc-ddea-11e7-8c2a-8f75989e06e2.png)

### The `Flex` Property
* "What do we do with the extra space, and/or what do I do when I don't have enough space?"
* `flex` property is applied on a flex item, not the container
* Actually consists of three properties: `flex-grow`, `flex-shrink`, and `flex-basis`
* Default is `auto`, which just makes flex item the width of the content inside of it
* `flex: 1` is the equivalent of `flex: 1 1 1`

    base case:

    ![screen shot 2017-12-10 at 9 18 02 pm](https://user-images.githubusercontent.com/15662012/33816726-d903e90a-ddef-11e7-9fc2-c307f42c27f8.png)

    `flex: 1` on all boxes:

    ![screen shot 2017-12-10 at 9 18 35 pm](https://user-images.githubusercontent.com/15662012/33816727-da615f44-ddef-11e7-9717-b4632a1179d6.png)
    * each flex item takes up the same amount of extra space available

    with the following CSS:
    ```
    .box {
        flex: 1;
    }
    .box2 {
        flex: 2;
    }
    ```

    ![screen shot 2017-12-10 at 9 23 10 pm](https://user-images.githubusercontent.com/15662012/33816788-5c821c16-ddf0-11e7-99fa-790d3a14cb99.png)
    * box2 takes up twice as much extra space as the rest of the boxes

    with the same CSS as above, and a smaller screen (this is incorporating the `flex-shrink` property, which would be the second input):
    ![screen shot 2017-12-10 at 9 27 21 pm](https://user-images.githubusercontent.com/15662012/33816852-f2ef5da8-ddf0-11e7-979f-fdcc4b1f8b99.png)

    specific `flex` properties on different boxes:

    ![screen shot 2017-12-10 at 9 04 58 pm](https://user-images.githubusercontent.com/15662012/33816451-d8c5da7c-dded-11e7-9f9a-f8e5e04add62.png)
    * box5 takes up 3 times as much space as all the boxes with `flex: 1`, and box2 takes up two times as much space as the boxes with `flex: 1`