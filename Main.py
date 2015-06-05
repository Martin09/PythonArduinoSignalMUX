# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 13:50:03 2015

@author: Martin Friedl
"""

from pyfirmata import ArduinoMega, util

#2D List for the arduino control pins of the multiplexer
#Inputs and outputs encoded into the position of the index in the 2D list
#list_MUX[InputID][OutputID]
list_MUX = [[5,3],
            [4,2]]
dict_GND = {"1":24,"2":22}

def discAll():
    print "Disconnecting all equipment..."
    for i in [item for sublist in list_MUX for item in sublist]: #Flatten the list
        if i <= 1: continue
        board.digital[i].write(0)
    print "Done!"
    
def discOutputs(inputID):
    for i in list_MUX[inputID-1]: #Loop over all outputs for that input
        if i <= 1: continue
        board.digital[i].write(0)

def connSignals(inputID,outputID):
    discOutputs(inputID) #Disconnect all other outputs first
    pin = list_MUX[inputID-1][outputID-1]
    print "Turning on pin " + str(pin)
    board.digital[pin].write(1) #Connect new output
    
def ground(outputID):
    pin = dict_GND[str(outputID)]
    board.digital[pin].write(0)
    
def unground(outputID):
    pin = dict_GND[str(outputID)]
    board.digital[pin].write(1)

if __name__ == '__main__':
    board = ArduinoMega('\\.\COM3')
    connSignals(1,1)




