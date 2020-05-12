# Frames & Styles

The bulk of the system relies on subscreens that include a frame which contains the dialogue text. For longer text strings we want the frame background to get larger. For shorter text strings we want that background to shrink. Other than specifying a minimum size, we let the shown background expand to fit the text, forcing it to use linebreaks by just setting a maximum width.

First though we need to make sure the text itself uses some specific style settings. We need to make sure our bubble text does not use the default settings applied through various gui values.

## The Text Style

The standard Ren'Py dialogue styles are a bit more convoluted than basic styles as the system uses a named widget in the screen and uses keywords that include that name to alter any other defaults. The say screen includes a text widget with the id "what". After inheriting the usual text styles, that widget then takes styles passed using that keyword plus an underscore.

A Character can have parameters beginning with what_
```py
define e = Character("Eileen", what_color="#D89")
```
A dialogue can have keywords beginning with what_
```py
    e "Hello World" (what_color="#D45")
```


## Styling Frames

That frame
