

# Electric guitar compressor pedal



## Overview / motivation

-  (E.g. wanted to improve PCB design and part sourcing with)

- Logistics of ordering parts for a project (BOM management)

For a long time I have wanted to build my own electric guitar pedal. The concept of an audio compression always appealed to me both in terms of how audio compression circuits operate as well as an audio effect to use with my guitar. Audio compressors are devices which reduce the volume of a signal when a loud sound spike occurs while leaving the signal unaffected the rest of the time (basically). This has the effect of reducing the dynamic range of a signal, which means the volume of quiet sounds and loud sounds is reduced.

While sifting  through articles about different compression circuits I stumbled across an <a href="http://www.valvewizard.co.uk/engineersthumb2.html" target="_blank">article by The Valve Wizard</a> which features a compression circuit called the engineers thumb which has several advantages compared to more common designs. The  design includes options for all five of the controls commonly found in an audio compressor circuits. Attack, release, threshold, ratio, and level.

The goal for the project was to get better at the whole design process. To start with just a schematic, then design all of the necessary hardware based on that, package everything neatly into an enclosure and finally document the project.

<img src="images/banner.png" alt="Front view of robot" style="width: 100%;">

## Circuit overview and PCB  design

The <a href="http://www.valvewizard.co.uk/engineersthumb2.html" target="_blank">article</a> written by The Valve Wizard has has a good description on the operation of the circuit, I will provide however provide a simpler explanation here. The signal from the guitar is fed into an opamp set up with negative feed back. In the feedback loop of this opamp circuit is an OTA or operational transconductance amplifier. This device acts as a current controlled resister. A resistor in an opamp feedback loop sets the gain for the circuit meaning that this part of the circuit is a current controlled amplifier. There is another circuit operating which measures the volume of the input signal and outputs a current source to the OTA. In this way, we have constructed a circuit which amplifies an audio signal with a gain dependent on its loudness at the input. Reducing the gain of the circuit when a loud sound, for example a big strum of the guitar comes along while leaving the volume of quieter sounds, for example single note soloing on a guitar, relatively unchanged.

<img src="images/schematic.jpg" alt="Front view of robot">



## Packaging / construction and  interface



## Conclusion (things  learnt, possible changes) and sound clip?

The hardest part of the design process seems to be interfacing between the PCB and external components. 
