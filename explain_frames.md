# Frames & Styles

The bulk of the system relies on subscreens that include a frame which contains the dialogue text. For longer text strings we want the frame background to get larger. For shorter text strings we want that background to shrink. Other than specifying a minimum size, we let the shown background expand to fit the text, forcing it to use linebreaks at the default maximum width setting or at a different size by passing a value.

First though we need to make sure the text itself uses some specific style settings. We need to make sure our bubble text does not use the default settings applied through various gui values.

## The Text Style

The standard Ren'Py dialogue styles are a bit more convoluted than basic styles as the system uses named widgets in the screen and then uses keywords that include those names to alter any default styles applied to those named widgets.

The widget in the say screen that we are interested in is a text widget with the id "what". After inheriting the usual text styles, that widget then takes styles passed using that keyword plus an underscore.

A Character can have parameters beginning with what_ and dialogue can have keywords beginning with what_
```py
define e = Character("Eileen", what_color="#D89")
# or
label start:
    e "Hello World" (what_color="#D45")
```

There are two main properties that we want to alter. We want the `xsize` and `align` values to be `None` and `(0, 0)` respectively.

Though there are a number of ways we could achieve that, the simplest is just to write a base style and tell all our Characters who use the bubbles to use that style. We can then tweak other `what_` settings as desired.
```py
style bubble_speech_text:
    xsize None # needed - otherwise it uses a gui setting
    align (0,0) # also likely needed

    # You could include your standard font specific stuff
    color "#F00"
    # font ""
    kerning -1.0
    size 26
    bold True
    # etc etc

## Define the Character, set the screen they use, tell them which style to use for the "what" widget
define speech_bubble_k = Character(
    "Kaori", 
    screen="bubble_say", 
    what_style="bubble_speech_text",
    what_color="#FDD")
```
These now make sure that the dialogue text does not try to take the screen width or sit at an offset.

## Styling Frames

Now we have made sure our text is appearing in a suitable rectangle we can handle how our frames respond to that (variable size) area.

At a basic level, every subscreen is just:
```py
screen bubble_subscreen(who, **kwargs):

    style_prefix "bubble_speech_baseright" # This is actually passed through keywords
    
    fixed:

        pos (450, 320) # Our x, y position, also through keywords

        frame:

            text "The Text" # Actually transcluded from the parent screen
```
In order to get the `frame:` there to have a nice background (that expands to fit the contained text) we use a style beginning with the prefix and ending with `_frame`
```py
style bubble_speech_baseright_frame:

    # our background picture
    background Frame(
        "images/speech_bubble.png", 
        left = Borders(32, 33, 88, 80)
        )

    # These are the distance between the text area and frame outer edge
    left_padding 24
    top_padding 22
    right_padding 23
    bottom_padding 73
    # We *could* do all that in one line with
    # padding (24, 22, 23, 73) # (left, top, right, base)

    minimum (121, 114)

    # Now the anchor (the pixel of this widget to place at the stated pos)
    # This should generally reflect where the end of the tail lies
    anchor (1.0, 1.0)
    # You could add a slight offset if wanted (so show_pos is on the tail)
    offset (12, 7)
```
Let's take it one part at a time

So, the frame: has a background which is a Frame
