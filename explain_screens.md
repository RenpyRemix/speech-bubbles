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
    for idx, old_dialogue in enumerate(retained_dialogues):

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
Easier to pull this one out of the kwargs as we reference it quite often. It specifies how many additional dialogues this particular line is meant to remain showing for.
```py
        who,
        what,
        kwargs
```
Usual stuff so we have much of the information to redisplay this line should we want to.


