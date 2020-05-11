
                            ###################
                            #                 #
                            #     Styles      #
                            #                 #
                            ###################

# Characters who use the speech bubbles will need their what_style pointed
# at a style similar to this 
#
# The first two settings are quite important. They let the bubbles
# shrink to the text bounds and position the first letter

style bubble_speech_text:
    xsize None # needed - otherwise it uses a gui setting
    align (0,0) # also likely needed

    # just standard font specific stuff
    color "#F00"
    # font ""
    kerning -1.0
    size 26
    bold True


# A rotated version of the bubble image
image speech_bubble_90:
    # using contains so it rotates before crop
    contains:
        "images/speech_bubble.png"
        rotate_pad False
        transform_anchor True
        anchor (0.0, 1.0)
        rotate 90.0
    # crop (as rotation increased the size)
    crop (0, 0, 135, 130)


# Styles for the different frames
# Each direction the tail points uses different values so has its own style

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


style bubble_speech_baseleft_frame:

    # our background picture
    background Frame(
        Transform("images/speech_bubble.png", xzoom=-1),
        left = Borders(88, 33, 32, 80)
        )

    # The distance between content and outer edge (left, top, right, base)
    padding (23, 22, 24, 73)

    minimum (121, 114)
    anchor (0.0, 1.0)
    offset (-12, 7)


style bubble_speech_topright_frame:

    # our background picture
    background Frame(
        Transform("images/speech_bubble.png", yzoom=-1), 
        left = Borders(32, 80, 88, 33)
        )

    # The distance between content and outer edge (left, top, right, base)
    padding (24, 73, 23, 22)

    minimum (121, 114)
    anchor (1.0, 0.0)
    offset (12, -7)


style bubble_speech_topleft_frame:

    # our background picture
    background Frame(
        Transform("images/speech_bubble.png", zoom=-1),
        left = Borders(88, 80, 32, 33)
        )

    # The distance between content and outer edge (left, top, right, base)
    padding (23, 73, 24, 22)

    minimum (121, 114)
    anchor (0.0, 0.0)
    offset (-12, -7)



style bubble_speech_leftbase_frame:

    # our background picture
    background Frame(
        "speech_bubble_90",
        left = Borders(80, 32, 33, 88)
        )

    # The distance between content and outer edge (left, top, right, base)
    padding (73, 24, 22, 23)

    minimum (114, 121)
    anchor (0.0, 1.0)
    offset (-7, 12)


style bubble_speech_lefttop_frame:

    # our background picture
    background Frame(
        Transform("speech_bubble_90", yzoom=-1), 
        left = Borders(80, 88, 33, 32)
        )

    # The distance between content and outer edge (left, top, right, base)
    padding (73, 23, 22, 24)

    minimum (114, 121)
    anchor (0.0, 0.0)
    offset (-7, -12)


style bubble_speech_righttop_frame:

    # our background picture
    background Frame(
        Transform("speech_bubble_90", zoom=-1), 
        left = Borders(33, 88, 80, 32)
        )

    # The distance between content and outer edge (left, top, right, base)
    padding (22, 23, 73, 24)

    minimum (114, 121)
    anchor (1.0, 0.0)
    offset (7, -12)


style bubble_speech_rightbase_frame:

    # our background picture
    background Frame(
        Transform("speech_bubble_90", xzoom=-1), 
        left = Borders(33, 32, 80, 88)
        )

    # The distance between content and outer edge (left, top, right, base)
    padding (22, 24, 73, 23)

    minimum (114, 121)
    anchor (1.0, 1.0)
    offset (7, 12)

# Just one to test we can pass (show_type="bubble_thought") and have it
# pick up a different style
style bubble_thought_baseright_frame is bubble_speech_baseright_frame:
    alt "Thinking"

                            ####################
                            #                  #
                            #     Screens      #
                            #        &         #
                            #      Python      #
                            #                  #
                            ####################
                # 
                # You probably will not need to edit this part
                #
                # Except maybe the callback if you want the default
                # values to be different

default retained_dialogues = []

init python:

    # This is just a list of style names that we want to remember for when
    # multiple dialogues (bubbles) appear at once
    retained_styles = (
        renpy.screenlang.text_property_names 
        + renpy.screenlang.position_property_names)


    #This function gets called after each dialogue is shown
    # It is responsible for calculating what will be shown with the
    # next dialogue
    def hide_dialogue(current_dialogue=None, screen="bubble_say"):
        """
        Decrease all `retain` values by one and rebuild global
        shown_dialogues only from those set to still be shown

        Then add the current dialogue if it has been set to retain
        """
        global retained_dialogues

        next_retained_dialogues = []

        for k in retained_dialogues:

            k[1] -= 1

            if k[1] > 0:

                next_retained_dialogues.append(k)

        retained_dialogues = next_retained_dialogues

        if current_dialogue and not current_dialogue[0][0].endswith('.rpym'):

            # This is where you could add a feature so one dialogue could 
            # alter setting for a retained dialogue (such as move it)

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


    # We use this callback so we can use simple arguments rather than
    # keywords each time
    def say_arguments_callback(who, *args, **kwargs):

        if hasattr(who, "screen") and who.screen == "bubble_say":

            # First we convert any passed args into kwargs 
            # (if the named kwarg has not been set)
            #
            # Args are a utility to pass common values quickly
            # (xpos, ypos, tail)

            if not "show_pos" in kwargs:
                # Default POS as a list Not tuple
                kwargs['show_pos'] = [800, 400] 

                if args and args[0] is not None:
                    kwargs['show_pos'][0] = args[0]
                if len(args) > 1 and args[1] is not None:
                    kwargs['show_pos'][1] = args[1]

            if not "show_tail" in kwargs:
                # Default tail style
                kwargs['show_tail'] = 'baseright' 

                if len(args) > 2 and args[2] is not None:
                    kwargs['show_tail'] = args[2]

            # You could amend to pass others as args too

            kwargs['show_type'] = kwargs.get('show_type', "bubble_speech")
            kwargs['show_xmax'] = kwargs.get('show_xmax', 320)
            #kwargs['show_xmin'] = kwargs.get('show_xmin', 0)

        kwargs['interact'] = kwargs.get('interact', True)

        return (), kwargs

    config.say_arguments_callback = say_arguments_callback


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



screen bubble_subscreen(who, **kwargs):

    # Each line of dialogue is shown in one of these subscreens
    # To use the correct Frame style we can pass keywords
    # show_type = the prefix part of the style
    # show_tail = the suffix part of the style
    #
    # The prefix_suffix then can use _frame as a style name

    style_prefix "{}_{}".format(kwargs['type'], kwargs['tail'])
    
    fixed:

        pos kwargs['pos']

        frame:

            xmaximum kwargs['xmax']

            # set the min width as show_xmin if passed else use default
            # (do not set smaller than the frame settings though)
            if "xmin" in kwargs:
                xminimum kwargs['xmin']

            # this single word tells this screen where to use 
            # the indented widgets/attributes (the text part)
            transclude

        if check_bubble_positions:
            add Solid('#FFF', xysize=(2, 40), anchor=(1, 20))
            add Solid('#FFF', xysize=(40, 2), anchor=(20, 1))

# Utility settings to draw a white cross at the specified 'show_pos'
# Maybe useful to setup Frame styles or fine tune positions
default check_bubble_positions = False

# On/Off toggle of the white cross using [Alt] + [c] keys together
init python:

    if config.developer:

        config.underlay.append(
            renpy.Keymap(
                alt_K_c = lambda: renpy.run(
                    ToggleVariable("check_bubble_positions"))))







                            #####################
                            #                   #
                            #     Characters    #
                            #         &         #
                            #       Sample      #
                            #                   #
                            #####################





define speech_bubble_a = Character("Amber",
                     screen="bubble_say", 
                     what_color="#282", 
                     what_style="bubble_speech_text",
                     show_tail="leftbase")

define speech_bubble_k = Character("Kaori", 
                     screen="bubble_say", 
                     who_color="#FDD", 
                     what_style="bubble_speech_text")


init python:

    config.label_overrides['start'] = "speech_bubble_example"

label speech_bubble_example:

    $ quick_menu = False

    window hide

    scene expression "#777"

    speech_bubble_k """A few lines showing the
    speech bubble system in action...""" (950, 300, "righttop")

    speech_bubble_a "Style default (baseright)
    \nYou can press Alt+C to show the used pos" (640, 320, show_xmax=500)

    speech_bubble_k "Style baseleft" (640, 320, "baseleft")

    speech_bubble_a "Style leftbase" (640, 320, "leftbase")

    speech_bubble_k "Style lefttop" (640, 320, "lefttop")

    speech_bubble_a "Style topleft" (640, 320, "topleft")

    speech_bubble_k "Style topright" (640, 320, "topright")

    speech_bubble_a "Style righttop" (640, 320, "righttop")

    speech_bubble_k "Style rightbase" (640, 320, "rightbase")

    speech_bubble_a "... and back to the game" (
        640, 320, show_type="bubble_thought")

    $ del config.label_overrides['start']

    jump start
