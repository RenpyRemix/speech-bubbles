# Using the Speech Bubbles system

So, you've read through and mostly understand how the system works, perhaps even tweaked the styles or extended them to add in your own thought bubbles or other other designs.

Now you want to get your characters using the system.

First we need to tell each Character that it should be using the amended `what_style` and the new `screen`.
```py
define speech_bubble_k = Character(
    "Kaori", 
    screen="bubble_say",
    what_style="bubble_speech_text")
```
Those are the name of the parent screen and the style for the text. You can also add in default settings for other what_ values as well as values passed to the screen (prefixed by `show_`). More details on that after covering the available settings.

## Args and Keyword Args

Each line of dialogue can pass arguments into the system to control how it is shown on the screen. There are default values for any not supplied, just so we do not have to include every setting on every dialogue line. These can be found (and adjusted) in the `say_arguments_callback` function.

The most commonly used settings can be supplied as positional arguments.
```py
    speech_bubble_k "Hello World" (650, 300, "righttop")
```
No need to tell it what each one is, it just knows that three optional arguments can be passed and, if they are passed, they relate to `(xpos, ypos, tail)`.

We could adjust the position and use default tail ("baseright") by just passing the first two.

```py
    speech_bubble_k "Hello World" (650, 300)
```

These values can also be passed by full keyword, along with the others here:
### Position
```py
    # change the xpos of the fixed
    e "..." (show_xpos = 140)
    
    # change the ypos of the fixed
    e "..." (show_ypos = 100)

    # change the combined pos of the fixed
    e "..." (show_pos = (140, 100))
```
### Size
```py
    # change the maximum width of the frame (allow it to expand to this width)
    e "..." (show_xmax = 440)

    # change the minimum width
    e "..." (show_xmin = 440)
    # note: The frame itself has an xminimum (so the background pic does not shrink and look odd)
    # This setting is more useful when it matches show_xmax in order to use things like extend
    # without the bubble changing size between each showing
```
### Style
```py
    # change the style prefix
    e "..." (show_type="bubble_thought")
    # this will use style bubble_thought_{show_tail}_frame
    
    # change the tail style (can be passed as the third argument)
    e "..." (show_tail="baseleft")
    # this will use style {show_type}_baseleft_frame
```
### Retain

This setting just uses an integer to state how many times this line is reshown for.
```py
    # tell it to retain for one extra line
    e "..." (show_retain = 1)
    l "..." # still showing the e line as well
    l "..." # now the e line is hidden
```

