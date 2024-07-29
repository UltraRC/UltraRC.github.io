# Oscilloscope Graphics

## Project Overview

It has been a common trick for a long time to use an analog oscilloscope to draw shapes and patterns to its display. This works by applying two voltages to channels 1 and 2 of the scope to control the horizontal and vertical position of the oscilloscopes electron beam. When the beam is moved quickly from one place to another, it leaves behind a bright glowing trail of green light which quickly disappears.

The idea came to mind that I could use the digital to analog converters (DAC) of a micro-controller to generate two voltages which could be used to control the position of the beam on the scope. I used an ESP32 devlopment board which has two 10-bit DACs built in. This provides 2^10 or 1024 different voltages between 0V and 3.3V for both X and Y.

## First Program!
After connecting the micro to the scope, the only thing left to do is write some code! The first program which I wrote was a basic 2D particle in a box physics simulation. The particle was given a mass and initial velocity, and with collision handling and gravity was implimented, a rather convincing "bouncing ball in a box" simulation was created.

<iframe width="560" height="315" src="https://www.youtube.com/embed/lEnchWlrA0M?si=DdLEtIfPl3doS2ac" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="width: 70%; height: 350px; margin: 0 auto; display: block;"></iframe>

## Going Further
While the particle simulation is a interesting, I wanted to go further. I wanted to draw lines and shapes. I first tried to