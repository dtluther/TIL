## Vanilla JS 30
### CSS Variables
##### Tricks
* Input type `range` for sliders
* CSS vars are declared on some sort of element
    * `:root` in our case:
        ```
        <style>
            :root {
            --base: #3493ca;
            --spacing: 10px;
            --blur: 10px;
            }

            img {
            padding: var(--spacing);
            background: var(--spacing);
            filter: blur(var(--blur));
            }

            .hl {
            color: var(--base);
            }
        ```
    * CSS vars are declared with "--" in front of them
    * Use `var()` to invoke a CSS var
* Can create any type of data attribute in an HTML element by prefixing it with "data-":
    * `<input type="range" name="spacing" min="10" max="25" value="10" data-sizing="px">`
        * Can view all data attributes of an element using the `#dataset` method, which provides an object of all of the attributes:
        ```
        <script>
            const inputs = document.querySelectorAll('.controls inputs');

            function handleUpdate() {
                const data = this.dataset;
            }

            inputs.forEach(input => input.addEventListener('mousemove', handleUpdate));
        ```
* Can access the root using `document.documentElement`
* Can update CSS property using `#setProperty`:
    ```
    document.documentElement.style.setProperty(`--${this.name}`, ${this.value});
    ```
* If I change a CSS var for a specific element, it will override the root var, but **ONLY** for that element