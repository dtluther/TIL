## Vanilla JS 30
### 02 - Clock Update
##### Questions to Answer
* Why does transform with a different parameter overwrite the entire transform? i.e. in the below scenario, I had to include the `rotate(90deg)` parameter again when making the translate specification to only the hour hand.
```
.hand {
      width:50%;
      height:6px;
      background:black;
      position: absolute;
      top:50%;
      transform-origin: 100%;
      transform: rotate(90deg);
      transition: all 0.05s; 
      transition-timing-function: cubic-bezier(0.07, 2.00, 0.3, 1.01); /* Used this to create the
      snapping of clock hands. Can edit the function by clicking on box in chrome dev tools. */
    }

    #hour-hand {
      width: 35%;
      transform: translateX(43%) rotate(90deg);
    }
```
