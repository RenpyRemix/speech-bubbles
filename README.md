# Speech Bubbles

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
- Create the subscreen and allow it to take parameters so each can display differently
- Include a system wherein the subscreen parameters can be retained, allowing it to be reshown during the following dialogue
- Adjust our Characters so they use the new screen say

The overview of the screen system is explained in [explain_screens.md!](explain_screens.md)

The styling and frames are explained in [explain_frames.md!](explain_frames.md)




Background: https://pixabay.com/illustrations/landscape-nature-summer-forest-4026168/

Sprites: 
  - Kaori: https://www.deviantart.com/kid-blue/art/female-teacher-1-274513797
  - Amber: https://www.deviantart.com/kid-blue/art/girl-in-uniform-1-274040211
