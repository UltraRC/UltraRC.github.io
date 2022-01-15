# Electric guitar compressor pedal



## Overview / motivation

-  (E.g. wanted to improve PCB design and part sourcing with)

- Logistics of ordering parts for a project (BOM management)

For a long time I have wanted to build my own electric guitar pedal. The concept of an audio compression always appealed to me both in terms of how audio compression circuits operate as well as an audio effect. Audio compressors are devices which reduce the volume when a loud sound occurs while leaving the signal unaffected the rest of the time (basically). This has the effect of reducing the dynamic range of a signal, which means the volume of quiet sounds and loud sounds is reduced.

While sifting  through articles about different compression circuits I stumbled across an <a href="http://www.valvewizard.co.uk/engineersthumb2.html" target="_blank">article by The Valve Wizard</a> which features a compression circuit called the engineers thumb which has several advantages compared to more common designs like the MXR Dynacomp compressor pedal. The  design includes options for all five of the controls commonly found in an audio compressor circuits. Attack, release, threshold, ratio, and level.

The idea of this project was to take this pre-existing circuit, design the PCB and get that manufactured.  After this package all of the components neatly into an enclosure with knobs and switches.

<img src="images/banner.png" alt="Front view of robot" style="width: 100%;">

## Circuit overview and PCB  design

The <a href="http://www.valvewizard.co.uk/engineersthumb2.html" target="_blank">article</a> written by The Valve Wizard has has a good description on the operation of the circuit, I will provide however provide a simpler explanation here. The signal from the guitar is fed into an opamp set up with negative feed back. In the feedback loop of this opamp circuit is an OTA or operational transconductance amplifier. This device acts as a current controlled resister. A resistor in an opamp feedback loop sets the gain the circuit meaning that this part of the circuit is a current controlled amplifier. There is another circuit operating which measures the volume of the input signal and outputs a current source to the OTA which is dependant on the volume of the audio input. In this way, we have constructed a circuit which amplifies an audio signal with a gain dependant on its loudness at the input. 

## Packaging / construction and  interface



## Conclusion (things  learnt, possible changes) and sound clip?

