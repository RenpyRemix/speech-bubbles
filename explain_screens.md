# Speech Bubbles Overview

So, let's start with the amended `screen say` as this is the first step in the process when a line of dialogue is shown.

```py
screen bubble_say(who, what, **kwargs):

    # This is the main container screen
    # It uses child screens to display each bubble, one for 
    # each dialogue that is set to be shown at this time

    # A tuple of information about the current dialogue line
    $ current_dialogue = (
        renpy.get_filename_line(),
        kwargs.pop('retain', 0),
        who,
        what,
        kwargs )

    # First the older (retained) dialogues
    for old_dialogue in retained_dialogues:

        $ old_who, old_what, old_kwargs = old_dialogue[2:]

        use bubble_subscreen(old_who, **old_kwargs):

            # Just standard Text here, no id needed
            # Styled to match how the 'retained' line was shown
            add Text(old_what, **old_kwargs['what_style'])

    # The current line (including the "what" id)
    use bubble_subscreen(who, **kwargs):
    
        text what id "what"

    # When this screen is hidden (at the next interaction from the player)
    # we pass the tuple of current dialogue info to the function
    on "hide":

        action Function(hide_dialogue, current_dialogue)
```
First you will notice that we build a sequence of information about the currently shown line. This includes:
```py
        renpy.get_filename_line(),
```
So we can check the line is real and not just a pre-game prediction
```py
        kwargs.pop('retain', 0),
```
Easier to pull this one out of the kwargs and store it separately as we reference it quite often. It specifies how many additional dialogues this particular line is meant to remain showing for.
```py
        who,
        what,
        kwargs
```
Usual stuff so we have much of the information to redisplay this line should we want to.

Next the screen iterates through any previous dialogues that were set to retain and displays them by transcluding a simple text widget to the subscreen. That widget is styled from retained styles that we stored when the line was first displayed. It is just a simple text as we cannot have more than one widget with the id "what" in the screen.

Next we display the current line by transcluding the normal text widget (with the id "what") into another copy of the subscreen. 

Once the line has been shown, we hook into the `on "hide"` event of the screen in order to pass all the information we have about the current dialogue to a named Python function. This means, when the screen is hidden, we know that function is going to run once with all the details we collected about the current dialogue passed to it.

## The subscreen

Just a basic screen that takes the sayer name (just in case you want to display it) and the keyword arguments that control the display. The simple version here just contains a fixed (for positioning) which contains a frame (for background styling) which contains the transcluded content.

There are also a few lines which add a toggle-able white cross to help highlight the passed position.

## The Python function

```py
    def hide_dialogue(current_dialogue=None, screen="bubble_say"):
```
This is our Python function that we call after the dialogue has been seen. We pass it the contents of the info tuple that we created in the screen along with the name of the screen
```py
        global retained_dialogues

        next_retained_dialogues = []

        for k in retained_dialogues:

            k[1] -= 1

            if k[1] > 0:

                next_retained_dialogues.append(k)

        retained_dialogues = next_retained_dialogues
```
First we look at the existing retained dialogues, decrease their `retain` value by one, check if they should be shown again and rebuild the global list with only those that should be reshown.
```py
        if current_dialogue and not current_dialogue[0][0].endswith('.rpym'):

            if current_dialogue[1] > 0:

                # retain this one, so add it to the global

                # first mirror the style applied to the text and add it
                # to the kwargs

                widget = renpy.get_widget(screen, 'what')
                if widget:
                    widget_style = {
                        k : getattr(widget.style, k)
                        for k in dir(widget.style)
                        if k in retained_styles
                    }
                    current_dialogue[-1]['what_style'] = widget_style

                retained_dialogues.append(list(current_dialogue))
```
Then we check our current dialogue, firstly making sure it is not just being predicted.

If the current dialogue is set to `retain` we duplicate the styles it uses and add it to the global retained_dialogues list.
To retain the styles we simply find the widget (we passed in the screen name and know it uses the id "what") and then read through the `.style` object to pull out the names and values we want (text properties and positional properties).

So, basically just check what is going to be shown again and build a list containing all the information we need for each line.

## The Say Arguments Callback

We *could* dispense with this part and solely pass all variable values using keywords. We could add `(show_xpos=100, show_ypos=200)` on a line to tell it to use those values. It's easier just putting the values though `(100, 200)`, especially for those values that change most often.

We use `config.say_arguments_callback` to do this, re-interpreting the positional arguments in an output keyword dictionary.

#### You should note that default values for all the settings are created here.


### Navigation:

[Home](README.md)

The overview of the system is more fully explained in [Speech Bubbles Overview](explain_screens.md)

The styling and settings for frame backgrounds are explained in [Frames & Styles](explain_frames.md)

The parameters and usage guidelines are explained in [Using the Speech Bubbles system](explain_screens.md)
