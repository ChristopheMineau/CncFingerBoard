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
    "passDepth" : 0.3,
    "slotDepth" : 2,
    "bindingWidth" : 2,
    "numberOfGcodeJobs" :3,
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
$passes
G00 Z12'''

FRET_PASS = '''Z$z  F200.0
X$x  F400.0
'''

FOOTER = '''

G00 X0 Y0
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
                
    def calcFretWidth(self):
        ratio =  (self.parentFB.fret12Width - self.parentFB.nutWidth) / (self.parentFB.scale / 2)
        return (- self.y * ratio) + self.parentFB.nutWidth
    
    def getGcode(self, yShift=0):
        passes = ""
        even = True
        for z in self.parentFB.zs:
            if even:
                x = round(self.x2, 2)
                even = False
            else:
                x = round(self.x1, 2)
                even = True
            passes += Template(FRET_PASS).safe_substitute(x = x, z = z)
        return Template(FRET).safe_substitute(x0 = round(self.x1, 2), y= round(self.y - yShift, 2), passes = passes[:-1])
        
    def __str__(self):
        return f"Fret number {self.id} y={self.y} width= {self.width} x1={self.x1} x2={self.x2}" # + "\n" + self.getGcode()

class Operation:
    # Different fret ranges milled in different Gcode files
    TEXT0 = "Save the following Gcode to a .nc file and run it on the CNC.\n" + \
            " - Operation : set the Origin (Zero X,Y,Z) at the center of nut/Fret 0 and top of surface and mill all the frets at once.\n\n" 
    TEXT1 =  "Save the following Gcode to $n separate files and run them separately on the CNC.\n" + \
                " - Operation 1 : set the Origin (Zero X,Y,Z) at the center of nut/Fret 0 and top of surface and mill from fret $fret1 to $fret2.\n\n" 
    TEXT2 =  " - Operation $op : Move the fingerboard blank up along the Y axis on the bed of the CNC (keep the alignment !),\n" + \
                "                      then reset the Y Origin to the middle of the already milled fret $fret1.\n" + \
                "                      Then mill from fret $fret1 to fret $fret2.\n\n"
    
    def __init__(self, n, f1, f2, numberOfGcodeJobs):
        self.fret1 = f1
        self.fret2 = f2
        self.n = n
        self.numberOfGcodeJobs = numberOfGcodeJobs

    def getText(self):
        return self.getText1() if self.n==1 else self.getText2()

    def getText1(self):
        if self.numberOfGcodeJobs==1:
            return self.TEXT0
        else:
            return Template(self.TEXT1).safe_substitute(n = self.numberOfGcodeJobs,
                                                    fret1 = self.fret1,
                                                    fret2 = self.fret2,)  
    def getText2(self):
        if self.numberOfGcodeJobs==1:
            return ""
        else:
            return Template(self.TEXT2).safe_substitute(op = self.n,
                                                    fret1 = self.fret1,
                                                    fret2 = self.fret2,)    

class Fingerboard:
    def __init__(self, params):
        self.params = params
        self.name = params["name"]
        self.scale = params["scale"]
        self.nFrets = params["numberOfFrets"]
        self.nutWidth = params["nutWidth"]
        self.fret12Width  = params["12thFretWidth"]
        self.passDepth = params["passDepth"]
        self.slotDepth = params["slotDepth"]
        self.bindingWidth = params["bindingWidth"]
        self.numberOfGcodeJobs = params["numberOfGcodeJobs"]
        assert (self.numberOfGcodeJobs >= 1 and self.numberOfGcodeJobs <= 4) , "### ERROR : Number of operations must be between 1 and 4."
        self.zs = [-round(self.passDepth*i, 1) for i in range(int(self.slotDepth/self.passDepth)+1) ]
        if self.zs[-1]<self.slotDepth:
            self.zs.append(-self.slotDepth)
        self.frets = [Fret(i, self) for i in range(self.nFrets + 1)]
        self.operations = []
        fretsPerOp = round(self.nFrets / self.numberOfGcodeJobs)
        for o in range(1, self.numberOfGcodeJobs + 1):
            self.operations.append(Operation(o, (o-1)*fretsPerOp, o*fretsPerOp ,self.numberOfGcodeJobs))
        self.operations[-1].fret2 = self.nFrets
        
    def __str__(self):
        return f"Fretboard for instrument : {self.name}\n" + \
               f"Scale={self.scale} Number of frets={self.nFrets}\n" + \
               f"Nut width={self.nutWidth} 12th fret width={self.fret12Width} Binding width={self.bindingWidth}\n" + \
               "\n".join(f.__str__() for f in self.frets)
               
    def getGcode(self):
        gCode = '\n' * 10
        for o in self.operations:
            gCode += o.getText()

        for o in self.operations:
            gCode += f"(FILE {o.n} STARTS HERE)\n"
            gCode +=  Template(HEADER).safe_substitute(name = self.name,
                                                fret1 = o.fret1,
                                                fret2 = o.fret2,
                                                originFret = o.fret1, )
            y0 = self.frets[o.fret1].y
            for f in self.frets:
                gCode += f.getGcode(yShift=y0) if f.id >= o.fret1 and f.id <= o.fret2 else ""
            gCode +=  FOOTER
            gCode += f"(FILE {o.n} ENDS HERE)\n"
            gCode += '\n' * 10

        return gCode
               
    


if __name__ == "__main__":
    # test
    guitare = Fingerboard(Params1)
    print(guitare)
    print(guitare.getGcode())




