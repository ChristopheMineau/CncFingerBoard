#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
The classes in this package are meant to generate a gcode programm in order to mill the slots of a fingerboard using a small endmill

Work Zero is located at the center of the nut (Fret 0)
X is the fret axis
Y is the scale axis (positive towards the nut, negative towards the bridge)
Z is the spindle axis

@author: Christophe Mineau www.labellenote.fr
'''
VERSION = '1.0 29/05/2021'

from string import Template

Params1 = {
    "name" : "guitare folk",
    "scale" : 633,
    "nutWidth" : 43,
    "nutHeight" : 5,
    "12thFretWidth" : 53,
    "numberOfFrets" : 20,
    "slotDepth" : 2,
    "bindingWidth" : 2,
    }






HEADER = '''G00 G49 G40.1 G17 G80 G50 G90
G21
(Fingerboard $name)
(Milling  Frets $fret1 to $fret2)
(Please set the 0,0,0 point to the center of Fret $originFret, at the surface of the Fretboard blank)
(Y axis is the scale axis, milling will be done towards the negative Y direction)

M6 T5
M03 S10000
G00 Z12
'''

FRET = '''
X$x0 Y$y
G01 Z0.5  F300.0
X$x1 Z$z1  F200.0
X$x2  F400.0
Z$z2  F200.0
X$x1 F400.0
G00 Z12
'''

FOOTER = '''
M5 M9
M30
'''



class Fret:
    SemiTone = pow(2, 1./12)
    def __init__(self, id, parentFB):
        self.id = id
        self.parentFB = parentFB
        self.y = -(self.parentFB.scale - (self.parentFB.scale / pow(self.SemiTone, self.id)))
        self.width = self.calcFretWidth()
        self.x1 = (-self.width / 2) + self.parentFB.bindingWidth
        self.x2 = +self.width / 2  - self.parentFB.bindingWidth
        self.z = -self.parentFB.slotDepth
        
    def calcFretWidth(self):
        ratio =  (self.parentFB.fret12Width - self.parentFB.nutWidth) / (self.parentFB.scale / 2)
        return (- self.y * ratio) + self.parentFB.nutWidth
    
    def getGcode(self, yShift=0):
        return Template(FRET).safe_substitute(x0 = round(self.x1+5, 2),
                                              x1 = round(self.x1, 2),
                                              x2 = round(self.x2, 2),
                                              y = round(self.y + yShift, 2),
                                              z1 = round(self.z/2, 2),
                                              z2 = round(self.z, 2), )
        
    def __str__(self):
        return f"Fret number {self.id} y={self.y} width= {self.width} x1={self.x1} x2={self.x2}" # + "\n" + self.getGcode()

class Fingerboard:
    def __init__(self, params):
        self.params = params
        self.name = params["name"]
        self.scale = params["scale"]
        self.nFrets = params["numberOfFrets"]
        self.nutWidth = params["nutWidth"]
        self.fret12Width  = params["12thFretWidth"]
        self.slotDepth = params["slotDepth"]
        self.bindingWidth = params["bindingWidth"]
        self.frets = [Fret(i, self) for i in range(self.nFrets + 1)]
        
    def __str__(self):
        return f"Fretboard for instrument : {self.name}\n" + \
               f"Scale={self.scale} Number of frets={self.nFrets}\n" + \
               f"Nut width={self.nutWidth} 12th fret width={self.fret12Width} Binding width={self.bindingWidth}\n" + \
               "\n".join(f.__str__() for f in self.frets)
               
    def getGcode(self):
        gCode = '\n' * 10
        # First file from fret 0 to fret 12
        gCode += "Save the following Gcode to two separate files and run them separately on the CNC.\n" + \
                 " - First operation : set the Zero at the center for the nut/Fret 0 and mill from fret 0 to 12.\n" + \
                 " - Second operation : Move the fingerboard blank up along the Y axis on the bed of the CNC (keep the alignment !),\n" + \
                 "                      then reset the zero to the middle of the already milled fret 12.\n" + \
                 "                      Then mill from fret 12 to the last fret.\n\n"
        gCode += "(FILE 1 STARTS HERE)\n"
        gCode +=  Template(HEADER).safe_substitute(name = self.name,
                                              fret1 = 0,
                                              fret2 = 12,
                                              originFret = 0, )
        for f in self.frets:
            gCode += f.getGcode() if f.id <= 12 else ""
        gCode +=  FOOTER
        gCode += "(FILE 1 ENDS HERE)\n"
        gCode += '\n' * 10
        # second file from fret 12 to last fret 
        gCode += "(FILE 2 STARTS HERE)\n"
        gCode +=  Template(HEADER).safe_substitute(name = self.name,
                                              fret1 = 12,
                                              fret2 = self.nFrets,
                                              originFret = 12, )
        for f in self.frets:
            gCode += f.getGcode(yShift=self.scale/2) if f.id >= 12 else ""
        gCode +=  FOOTER
        gCode += "(FILE 2 ENDS HERE)\n"

        return gCode
               
    


if __name__ == "__main__":
    # test
    guitare = Fingerboard(Params1)
    print(guitare)
    print(guitare.getGcode())




