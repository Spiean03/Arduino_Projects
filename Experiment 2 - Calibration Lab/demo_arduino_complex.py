# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:27:51 2018
@author: Andreas Spielhofer
"""

import calibration as arduino
import numpy
import matplotlib.pyplot as plt
import os

print "Creating an arduino object a"
a = arduino.arduino(debug=0)

print "Calling a.out_buffer_length() to get maximum output vector length"
length =  a.out_buffer_length()
print "Output buffer can take maximum of %d entries" % length

print "Calling a.sampling_time(10000) to determine sampling frequency"
t_sample = a.sampling_time(10000)
f_sample = 1/t_sample;
print "Sampling frequency: %f Hz" % f_sample

# generate vector 0...length-1
index = numpy.fromiter(range(0,length),int)
# generate vector 0..2pi
x = index*2*numpy.pi/length
# generate time base (for plotting)
t = t_sample * index

print "About to characterize lowpass filter on pin 10"
print "Since the sampling frequency is %f Hz, and vector length is %d," % (f_sample, length)
print "a single cycle of a sine wave spanning the vector will have the frequency"
print "f_s/length = %f Hz, I denote this the fundamental frequency."
indexes = range(0,8)
harmonics = numpy.power(2,numpy.fromiter(indexes,int))
frequencies = f_sample / length * harmonics
amplitudes = numpy.zeros_like(frequencies)
phases = numpy.zeros_like(frequencies)
for i in indexes :
  print "Generating vectors for harmonic %d (%f Hz)" % (harmonics[i],frequencies[i])
  c = numpy.cos(harmonics[i]*x)
  s = numpy.sin(harmonics[i]*x)
  # generate sine wave to send to Arduino
  values = (128+127*c).round().astype(int)
  # send vector and read back response after 1 iteration
  print "calling a.analogWriteReadVector(10,0,values,iterations=1)"
  print "PWM output pin: 10, ADC input 0, values is vector of integer values to be written"
  iv = a.analogWriteReadVector(10,0,values,iterations=1)
  print "a.analogWriteReadVector has returned vector of ADC readings"
  print "Analyzing amplitude and phase of returned vector modeled as"
  print "iv = Amplitude cos(2*pi*%f Hz t + Phase)" % frequencies[i]
  sum_c = 2*numpy.sum(c*iv)/length
  sum_s = 2*numpy.sum(s*iv)/length
  amplitudes[i] = numpy.sqrt(sum_c*sum_c + sum_s*sum_s)
  phases[i] = numpy.arctan2(sum_s,sum_c)
  print "Amplitude = %f, Phase = %f"  % (amplitudes[i],phases[i])

fc = 70

plt.figure()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (ADC units)")
plt.plot(frequencies,amplitudes)

plt.figure()
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.plot(frequencies,phases)

def lowpass_amplitude(f,fc) :
  return 1/numpy.sqrt(1+numpy.power(f/fc,2))

def lowpass_phase(f,fc) :
  return numpy.arctan(f/fc)

print "Generating an arbitrary wave, raw, to demo amplitude phase correction"
# sketch Mount Royal
raw = numpy.zeros(length)
quanta = int(numpy.floor(length/9))
for i in range(0,length) :
  if i < quanta : raw[i] = 0
  elif i < 3*quanta : raw[i] = i-quanta
  elif i < 4*quanta : raw[i] = 5*quanta-i
  elif i < 6*quanta : raw[i] = i-3*quanta
  else : raw[i] = 9*quanta-i

print "Calculating amplitudes and phases of frequency components in wave, raw"
f_fund =  f_sample / length
fft = numpy.fft.rfft(raw)
amplitudes = numpy.sqrt(fft.real**2+fft.imag**2)*2/length
phases = numpy.arctan2(fft.imag,fft.real)

print "Constructing a wave, synth, which when sent through lowpass filter will resemble raw"
angle = numpy.fromiter(range(0,length),int)*2*numpy.pi/length
synth = numpy.zeros(length)
for i in range(1,length/2) :
  synth = synth + amplitudes[i]*numpy.cos(i*angle+phases[i]-lowpass_phase(f_fund*i,fc))/lowpass_amplitude(f_fund*i,fc)

# normalize wave to bounds of PCM
synth = synth - synth.min()
synth = synth * 255 / synth.max()

print "calling a.analogWriteVector(10,synth.astype(int))"
a.analogWriteVector(10,synth.astype(int))

print "Plot raw, which should be what appears on oscilloscope, and synth which is what is sent"
plt.figure()
plt.plot(raw)
plt.plot(synth)
plt.show()
