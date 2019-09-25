# AddNet
KiCAD AddNet action-plugin

Allows to add a new net on a already existing PCB.

## When use this tool (hopefully never!)

In the correct approach to electronic design, the normal workflow when you become aware that a new net is needed during PCB routing is:
- getting back on __EESchema__,
- apply the needed fixes,
- export it to the ```net``` file
- rebuild the connectivity in __PCBNew__.

In the real world and more specifically under some work dynamics/cicumstances (hurry hurry!) this workflow can be time wasting or disruptive.

The main *cases-of-use* for this tool are (assuming an intricate schematics as a basis or no schematics at all):
- I have not a schematics and I need to modify pcb design;
- I found a missing connection on my board (often caused by a non correctly designed footprint or symbol);
- I performed a number of pin net reassignment and/or change of footprint and I found a net missing;

In such cases getting back to __EESchema__ to fix  can be painful (or even unfeasible) and non error-free resulting in repeating the process more than once. Having a chance to create a brand new net can speed up the board routing. Prior writing this plugin I was usually doing this by text editing ```.kicad_pcb``` file by hand (not an error free practice but quite fast).
Of course, for the sake of the project, I fix all the mess the right way at a certain point, usually at the end of routing.

## How it works

After installing it (just clone this repo in your preferred plugin location) launch __KiCAD__ and click on ```Tools->External Plugins->AddNet``` a dilaog like the one below should appear:

![AddNet dialog](pictures/addnet_dialog.PNG?raw=true "AddNet dialog")

Just write down a suitable name (in the __net name__ textbox), select a module and a pad on which the net will apply, press __Ok__.
The plugin will create the new net and apply it to the selected pad.
The result is something like that:

![Addnet result](pictures/addnet_result.PNG?raw=true "AddNet result")

## Coding notes

If you are willing to make any modification to the GUI trough __wxFormBuilder__ (```addnet.fbp``` file) remember to modify this line (around line 21 ```addnet_gui.py```):
```
self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
```
In this way:
```
if sys.version_info[0] == 2:
 self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
else:
 self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
```
This modification allows the code to work with Python 2 (that's the standard KiCAD/Python distribution AFAIK), please note that you need to ```import sys```. 

## WireIt similarity

This tool share some similarity with __WireIt__ ```Connect with Airwire``` feature: unluckly I've become aware of __WireIt__ existance only after having coded my plugin.

## References
Some useful references that helped me coding this plugin:
1. https://sourceforge.net/projects/wxformbuilder/
2. https://wxpython.org/
3. http://docs.kicad-pcb.org/doxygen-python/namespacepcbnew.html
4. https://forum.kicad.info/c/external-plugins
5. https://github.com/KiCad/kicad-source-mirror/blob/master/Documentation/development/pcbnew-plugins.md

Tool I got inspired by:
- https://github.com/NilujePerchut/kicad_scripts/tree/master/teardrops

Very good tools makers:
- https://github.com/xesscorp/

## Greetings
Hope someone find my work useful or at least *inspiring* to create something else/better.

I would like to thank in particular:
- Qu1ck
- MitjaN
- NilujePerchut
- hildogjr

For having shared they knoledge of Python and KiCAD with me: Thanks! 

Live long and prosper!

That's all folks.

By[t]e{s}
 Weirdgyn
