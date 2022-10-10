from main import Keithly3390
from time import sleep

psu = Keithly3390()


#========= setup pulse
"""
shape: {SINusoid, SQUare, RAMP, NRAMp, TRIangle} (string)
amplitude: Voltage high in volts (float)
pulsewidth: how long you want the pulse (float)

"""

def setPulse(shape, amplitude, pulsewidth):
    # Setup carrier pulse settings
    psu.setVoltageLow(0)
    psu.setVoltageHigh(amplitude)
    psu.setPulsewidth(pulsewidth * 2)
    psu.setDutyCycle(50) # duty cycle in percent
    
    # Setup PWM
    psu.setPWMFunction(shape)
    psu.setPWMFrequency(1 / (pulsewidth * 2)) # Makes a half cycle


#====== Example pulse
setPulse('SQUare', 300e-3, 1)
psu.trigger()



#====== Test Scenario Loop
def testLoop():
    '''
    Loop through each pulse width and check the waveform is correct
    10s wait between each one for you to reset the oscilloscope trigger
    '''
    shapes = ['SINusoid', 'SQUare', 'RAMP', 'NRAMp', 'TRIangle']
    amplitudes = [100e-3, 200e-3, 300e-3]
    pulsewidths = [0.5, 1, 2]
    def testPulses():
            for shape in shapes:
                for amplitude in amplitudes:
                    for pulsewidth in pulsewidths:
                        setPulse(shape, amplitude, pulsewidth)
                        psu.trigger()
                        sleep(10)





