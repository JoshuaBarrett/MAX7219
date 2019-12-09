# Matrix Driver module for multiple displays

import RPi.GPIO as GPIO
import MatrixCharacters as CHARS
import time

dataPin = 19
clkPin = 23
loadPin = 24
channels = [dataPin, clkPin, loadPin]

decodeAddress = 0x09
intensityAddress = 0x0A
scanAddress = 0x0B
shutdownAddress = 0x0C
testAddress = 0x0F
noOpAddress = 0x00

displayCount = 3

def clk():
    GPIO.output(clkPin, 1)
    GPIO.output(clkPin, 0)

def load():
    GPIO.output(loadPin, 1)
    GPIO.output(loadPin, 0)

def sendBit(bit):
    GPIO.output(dataPin, bit)
    clk()

def formatToByte(value):
    return format(value, ('08b'))

def sendInstruction(address, data):
    instruction = formatToByte(address) + formatToByte(data)
    for b in instruction:        
        sendBit(int(b))    

def shutdownMode(mode):
    sendInstruction(shutdownAddress, (1-mode))

def testMode(mode):
    sendInstruction(testAddress, mode)

def scanMode():
    #Scan mode for matrix is always 7
    sendInstruction(scanAddress, 7)

def decodeMode():
    #Decode mode for matrix is always 0
    sendInstruction(decodeAddress, 0)

def intensityMode(intensityRating = 0x0A):
    sendInstruction(intensityAddress, intensityRating)

def noOp():
    sendInstruction(noOpAddress, 0)

def flatten(nestedArray):
    return [v for array in nestedArray for v in array]

def sendMessage(message, scanRate = 0.025):
    dataArray = flatten(message)
    #Pad message
    dataArray[:0] = [0 for _ in range(0, 8*displayCount)]
    dataArray += [0 for _ in range(0, 8*displayCount)]  
        
    for messagePointer in range(0, len(dataArray) - (displayCount * 8)):
        time.sleep(scanRate)
        for col in range(1, 9):
            for i in range(0, displayCount):
                sendInstruction(col, dataArray[messagePointer + (i * 8) + (col - 1)])
            load()

def initialiseChannels():
    GPIO.setmode(GPIO.BOARD)  
    GPIO.setup(channels, GPIO.OUT)
    GPIO.output(channels, GPIO.LOW)

def initialiseDisplays(numberOfDisplaysIn = 3):
    initialiseChannels()
    
    global displayCount    
    displayCount = numberOfDisplaysIn
    
    #Disable shutdown for all
    for _ in range(0, displayCount):
        shutdownMode(0)
    load()

    #Disable testmode for all
    for _ in range(0, displayCount):
        testMode(0)
    load()

    #Set Scan mode for all
    for _ in range(0, displayCount):
        scanMode()
    load()

    #Set decode mode for all
    for _ in range(0, displayCount):
        decodeMode()
    load()

    #Set intensity mode for all
    for _ in range(0, displayCount):
        intensityMode()
    load()

    #Clear Registers
    for _ in range(0, displayCount):
        noOp()
    load()

    #Clear Displays
    for i in range(1, 9):
        for _ in range(0, displayCount):
            sendInstruction(i, 0)
        load()

    
    







    



    
        

                  

    
