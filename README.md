# Speech Bubbles

#### Note: All you really need are the two files in [The game folder](game). Just one image and a small script file. They can be dropped into a new or existing project and a sample will run before label start.

So, you want a system where each line of dialogue can appear at a set position in a frame that looks like a comic book speech bubble?

You want all the normal Ren'Py dialogue things to still work... translation, styles, text tags, extend and everything else related to the line of speech.

You want the ability to show multiple bubbles at once, styled differently and you want a system that makes it easy to specify the settings for each line.

![Image of Speech Bubbles](explain_images/speech_bubbles.gif?raw=true "Thanks to:
Pixabay for the background
Kid Blue for the sprite images
Links at the end of this overview.")

# Speech Bubbles in Ren'Py

In order to achieve this, we need to handle several things:
- Create a new screen say that can use subscreens to show each line of dialogue
  - Creating a new screen lets us leave the normal one there if needed. 
  - This new screen cycles through all the dialogue lines (bubbles) it should show and passes the parameters of each to a used subscreen
- Create the subscreen and allow it to take parameters so each can display differently
  - Using say arguments like `e "Hello World" (450, 280, "topleft")` the used subscreen can be positioned at (450, 280) and use a style with tail at "topleft"
  - Additional keywords can be passed to adjust other settings
- Include a system wherein the subscreen parameters can be retained, allowing it to be reshown during the following dialogue
  - We use the `on "hide"` event of our new screen say to pass the current dialogue and settings to a function
  - That function determines what if anything is retained to be reshown with the following line and stores them in a global
- Adjust our Characters so they use the new screen say
  - This includes changing their `what_style` so they do not use default settings intended for large dialogue windows


### Important Reading:

The overview of the system is more fully explained in [Speech Bubbles Overview](explain_screens.md)

The styling and settings for frame backgrounds are explained in [Frames & Styles](explain_frames.md)

The parameters and usage guidelines are explained in [Using the Speech Bubbles system](explain_screens.md)

### Please note:

The way this approach works might not be suitable for complete beginners. It is a basic platform on which to build a system that might grow to include many other styles (such as thought clouds, jagged exclaimation bubbles, showing character names etc). As such it will likely require some knowledge of Ren'Py in order to extend it to your particular needs. 

Though I have tried to explain it as simply as possible, I will not be available to help extend it unless under a paid contract.
Basically, if you want it to do more, you are expected to know enough Ren'Py to handle that yourself (or consider paying someone)


### Credits

Background: https://pixabay.com/illustrations/landscape-nature-summer-forest-4026168/

Sprites: 
  - Kaori: https://www.deviantart.com/kid-blue/art/female-teacher-1-274513797
  - Amber: https://www.deviantart.com/kid-blue/art/girl-in-uniform-1-274040211
