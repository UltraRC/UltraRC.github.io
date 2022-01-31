

# Electric guitar compressor pedal

## 1 - Overview / motivation

-  (E.g. wanted to improve PCB design and part sourcing with)

- Logistics of ordering parts for a project (BOM management)

For a long time I have wanted to build my own electric guitar pedal. The concept of an audio compression always appealed to me both in terms of how audio compression circuits operate as well as an audio effect to use with my guitar. Audio compressors are devices which reduce the volume of a signal when a loud sound spike occurs while leaving the signal unaffected the rest of the time (basically). This has the effect of reducing the dynamic range of a signal, which means the volume of quiet sounds and loud sounds is reduced.

While sifting  through articles about different compression circuits I stumbled across an <a href="http://www.valvewizard.co.uk/engineersthumb2.html" target="_blank">article by The Valve Wizard</a> which features a compression circuit called the engineers thumb which has several advantages compared to more common designs. The design includes options for all five of the controls commonly found in an audio compressor circuits, not least of which includes the option for all five controls. Attack, release, threshold, ratio, and level.

The goal for the project was to take this design and package it into a custom drilled enclosure with all the necessary switches, knobs and jacks. I also designed a custom PCB derived from the original circuit (more details later).

<figure>
        <img src="images/banner.png" alt="Front view of robot" style="width: 100%;">
        <figcaption>
            Figure 1.1 - Original schematic by The Valve Wizard
    </figcaption>
</figure>

## 2 - Circuit overview and PCB  design

The <a href="http://www.valvewizard.co.uk/engineersthumb2.html" target="_blank">article</a> written by The Valve Wizard has has a good description on the operation of the circuit, I will provide however provide an explanation here as well. The signal from the guitar is fed into an opamp (operational amplifier) set up with negative feed back. In the feedback loop of this opamp circuit is an operational transconductance amplifier or OTA for short. This device essentially acts as a current controlled resister. A resistor in an opamp feedback loop sets the gain for the circuit meaning that this part of the circuit is a current controlled amplifier. Changing the current flowing into the OTA changes its resistance which reduces the gain of the opamp circuit it is placed within. The output of this opamp circuit after passing through a volume potentiometer and a DC blocking capacitor is fed to the output.

There is another circuit operating on a separate branch of components which measures the amplitude of the input signal. This separate circuit outputs a current relative to this amplitude it is measuring to the OTA thereby adjusting the gain of the first opamp circuit by an amount dependant on the input amplitude. On of claimed advantages of this circuit design is that because the OTA is in the feedback loop of the first opamp circuit, when the gain of the OTA is at its highest, the opamp circuit gain is at its lowest. This means that at idle (opamp circuit is at highest gain) while no signal is being sent to the pedal, the OTA will be functioning at its lowest and because OTA's produce a lot of noise the overall noise of the circuit will be lower with this configuration.

<figure>
        <img src="images/schematic.jpg" alt="Front view of robot" width = "100%">
        <figcaption>
            Figure 2.1 - Original schematic by The Valve Wizard
    </figcaption>
</figure>





## 3 - Packaging / construction and  interface

Stages of design:

- PCB design
- Enclosure layout
- Enclosure

The first task to complete was the design of the PCB.

<figure>
        <img src="images/assemblyWithoutLid.png" alt="Front view of robot" width = "80%">
        <figcaption>
            Figure 3.1 - Render of whole assembly without lid
    </figcaption>
</figure>





<figure>
        <img src="images/pcb.jpg" alt="Front view of robot" width = "90%">
        <figcaption>
            Figure 3.2 - PCB's manufactured by JLC PCB
    </figcaption>
</figure>

## Conclusion (things  learnt, possible changes) and sound clip?

The hardest part of the design process seems to be interfacing between the PCB and external components. 