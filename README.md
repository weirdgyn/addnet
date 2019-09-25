# addnet
KiCAD Add Net plugin

Allows to add a net on a already existing PCB.

## When use this tool (hopefully never!)

In the correct approach to electronic design the normal workflow when a new net is needed you should get back on __EESchema__ and apply the needed fixes export it to the net file and rebuild the connectivity in __PCBNew__.
In the real world and more specifically under some work dynamics/cicumstances this workflow can be painful and time wasting.

The main cases-of-use for this ool are the following (assuming an intricate schematics as a basis or no schematics at all):
1. I have not a schematics and I need to modify pcb design;
2. I found a missing connection on my board (often caused by a non correcly designed footprint or symbol);
3. I performed a number of pin net reassignment and/or change of footprint and I found a missing net;

In such cases getting back to __EESchema__ to fix all this can be painful (or even unfeasible) and non error-free (resulting in repeating the process more than once). Having a chance to create a brand new net can speed up the board routing. Prior writing this plugin I was usually doing this by text editing ```.kicad_pcb file``` by hand.
Of course, for the sake of the project, I fix all the mess at a certain point (usually at the end of routing).

## How it works

![AddNet dialog](pictures/addnet_dialog.PNG?raw=true "AddNet dialog")

Just write down a net name (in the __netname__ textbox), select a module and a pad where to apply the net, press __Ok__.
The plugin will create the new net and apply it to the selected pad.
The result is something like that:

![Addnet result](pictures/addnet_result.PNG?raw=true "AddNet result")


By[t]e{s}
 Weirdgyn
