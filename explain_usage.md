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

Each line of dialogue can pass arguments into the system to control how it is shown on the screen 
