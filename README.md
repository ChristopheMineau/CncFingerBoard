# For the luthier shop with CNC : CncFingerBoard
This project is designed to provide a CNC program in order to mill the fret slots of a fretboard.
For this, you will need first a CNC machine and a suitable endmill (0.6mm diameter typically).
Depending on the scale of the instrument, and the size of the bed of your machine, you may need to divide the work into different jobs,
repositionning your fretboard blank between each job.
Doing so, you will be able to mill a full length fretboard even on a small bed CNC.

This project is a python3 project. You can run the program CncFingerboard.py either on a local python installation, or if you don't have one,
on a remote Web base environment like : https://www.online-python.com/

Different parameters are available, and must be changed in the program itself (work in progress, an operator interface will be done in the future, but you know ...)

# Setup
You need a blank for your fingerboard, it must be parallel, and its central axis must be set parallel to the Y axis.
If you intend to mill the fingerboard in more than one job, it is wise to fix on the bed, left or right to the blank, a straightedge.
When milling the additional jobs, you will have to relocate the blank in the upward direction along the straightedge, so that the last milled fret in the previous job comes in zero position.
This allows to mill a large fingerboard on a smaller CNC bed, splitting the work in 2, 3 or even 4 tasks, following the parameter  numberOfGcodeJobs (see below).

The Zero position on your CNC must be tuned at the top of the fingerboard, in the middle of the nut or fret 0 line.

In any case, read carefully the instructions from the printouts of the program !

# Parameters
In the CncFingerboard.py program, from line 17 you will find :
```
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
```
* Name : string giving the name of the instrument, will be provided as a comment in the generated Gcode
* Scale : scale in mm of the instrument
* Nut width : nut width in mm, from side to side.
* nutHeight : not used so far
* 12thFretWidth : width of the fingerboard (binding included if any) at the 12th fret
* numberOfFrets : number of frets (not taking into account a possible fret 0)
* passDepth : in mm, depth of cut for each pass
* slotDepth : in mm, full depth of the cut. Must be slightly taller than the foot of the fret
* bindingWidth : in mm, it's actually a margin between the edge of the fingerboard and the beginning of the cut.
* numberOfGcodeJobs : between 1 and 4 , number of jobs you want to divide the work into. Depends of the size of the bed of the CNC versus the scale of the instrument;
If you have a big enough CNC, you can do the work in one single job, otherwise use values 2, 3 or 4.
It will then create 1, 2 3 or 4 files you will have to save as separate gcode files and run separately.
Read carefully the instructions provided by the program.

# Example

Parameters :
```
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
```

Gives the following results :

```
Fretboard for instrument : guitare folk
Scale=633 Number of frets=20
Nut width=43 12th fret width=53 Binding width=2
Fret number 0 y=-0.0 width= 43.0 x1=-19.5 x2=19.5
Fret number 1 y=-35.527560072488086 width= 44.12251374636613 x1=-20.061256873183066 x2=20.061256873183066 
Fret number 2 y=-69.0611114171652 width= 45.18202563719321 x1=-20.591012818596607 x2=20.591012818596607   
Fret number 3 y=-100.7125691443988 width= 46.18207169492571 x1=-21.091035847462855 x2=21.091035847462855  
Fret number 4 y=-130.58756705206497 width= 47.12598948031801 x1=-21.562994740159006 x2=21.562994740159006 
Fret number 5 y=-158.78581016853036 width= 48.016929231233185 x1=-22.008464615616592 x2=22.008464615616592
Fret number 6 y=-185.4014075089155 width= 48.85786437626905 x1=-22.428932188134524 x2=22.428932188134524  
Fret number 7 y=-210.52318615518425 width= 49.65160145829966 x1=-22.82580072914983 x2=22.82580072914983
Fret number 8 y=-234.2349877082728 width= 50.40078950105127 x1=-23.200394750525636 x2=23.200394750525636
Fret number 9 y=-256.61594810163893 width= 51.107928849972794 x1=-23.553964424986397 x2=23.553964424986397
Fret number 10 y=-277.74076171008363 width= 51.77537951690628 x1=-23.88768975845314 x2=23.88768975845314
Fret number 11 y=-297.6799306352832 width= 52.405369056407054 x1=-24.202684528203527 x2=24.202684528203527
Fret number 12 y=-316.5000000000001 width= 53.0 x1=-24.5 x2=24.5
Fret number 13 y=-334.26378003624416 width= 53.56125687318307 x1=-24.780628436591535 x2=24.780628436591535
Fret number 14 y=-351.03055570858277 width= 54.09101281859661 x1=-25.045506409298305 x2=25.045506409298305
Fret number 15 y=-366.8562845721995 width= 54.59103584746286 x1=-25.29551792373143 x2=25.29551792373143
Fret number 16 y=-381.7937835260326 width= 55.062994740159006 x1=-25.531497370079503 x2=25.531497370079503
Fret number 17 y=-395.8929050842653 width= 55.508464615616596 x1=-25.754232307808298 x2=25.754232307808298
Fret number 18 y=-409.2007037544579 width= 55.92893218813453 x1=-25.964466094067266 x2=25.964466094067266
Fret number 19 y=-421.76159307759224 width= 56.32580072914983 x1=-26.162900364574917 x2=26.162900364574917
Fret number 20 y=-433.6174938541365 width= 56.70039475052564 x1=-26.35019737526282 x2=26.35019737526282










Save the following Gcode to 3 separate files and run them separately on the CNC.
 - Operation 1 : set the Origin (Zero X,Y,Z) at the center of nut/Fret 0 and top of surface and mill from fret 0 to 7.

 - Operation 2 : Move the fingerboard blank up along the Y axis on the bed of the CNC (keep the alignment !),
                      then reset the Y Origin to the middle of the already milled fret 7.
                      Then mill from fret 7 to fret 14.

 - Operation 3 : Move the fingerboard blank up along the Y axis on the bed of the CNC (keep the alignment !),
                      then reset the Y Origin to the middle of the already milled fret 14.
                      Then mill from fret 14 to fret 20.

(FILE 1 STARTS HERE)
G00 G49 G40.1 G17 G80 G50 G90
G21
(Fingerboard guitare folk)
(Milling  Frets 0 to 7)
(Please set the 0,0,0 point to the center of Fret 0, at the surface of the Fretboard blank)
(Y axis is the scale axis, milling will be done towards the negative Y direction)

M6 T5
M03 S10000
G00 Z12


X-19.5 Y0.0
G01 Z0.5  F300.0
Z-0.0  F200.0
X19.5  F400.0
Z-0.3  F200.0
X-19.5  F400.0
Z-0.6  F200.0
X19.5  F400.0
Z-0.9  F200.0
X-19.5  F400.0
Z-1.2  F200.0
X19.5  F400.0
Z-1.5  F200.0
X-19.5  F400.0
Z-1.8  F200.0
X19.5  F400.0
Z-2  F200.0
X-19.5  F400.0
G00 Z12

X-20.06 Y-35.53
G01 Z0.5  F300.0
Z-0.0  F200.0
X20.06  F400.0
Z-0.3  F200.0
X-20.06  F400.0
Z-0.6  F200.0
X20.06  F400.0
Z-0.9  F200.0
X-20.06  F400.0
Z-1.2  F200.0
X20.06  F400.0
Z-1.5  F200.0
X-20.06  F400.0
Z-1.8  F200.0
X20.06  F400.0
Z-2  F200.0
X-20.06  F400.0
G00 Z12

X-20.59 Y-69.06
G01 Z0.5  F300.0
Z-0.0  F200.0
X20.59  F400.0
Z-0.3  F200.0
X-20.59  F400.0
Z-0.6  F200.0
X20.59  F400.0
Z-0.9  F200.0
X-20.59  F400.0
Z-1.2  F200.0
X20.59  F400.0
Z-1.5  F200.0
X-20.59  F400.0
Z-1.8  F200.0
X20.59  F400.0
Z-2  F200.0
X-20.59  F400.0
G00 Z12

X-21.09 Y-100.71
G01 Z0.5  F300.0
Z-0.0  F200.0
X21.09  F400.0
Z-0.3  F200.0
X-21.09  F400.0
Z-0.6  F200.0
X21.09  F400.0
Z-0.9  F200.0
X-21.09  F400.0
Z-1.2  F200.0
X21.09  F400.0
Z-1.5  F200.0
X-21.09  F400.0
Z-1.8  F200.0
X21.09  F400.0
Z-2  F200.0
X-21.09  F400.0
G00 Z12

X-21.56 Y-130.59
G01 Z0.5  F300.0
Z-0.0  F200.0
X21.56  F400.0
Z-0.3  F200.0
X-21.56  F400.0
Z-0.6  F200.0
X21.56  F400.0
Z-0.9  F200.0
X-21.56  F400.0
Z-1.2  F200.0
X21.56  F400.0
Z-1.5  F200.0
X-21.56  F400.0
Z-1.8  F200.0
X21.56  F400.0
Z-2  F200.0
X-21.56  F400.0
G00 Z12

X-22.01 Y-158.79
G01 Z0.5  F300.0
Z-0.0  F200.0
X22.01  F400.0
Z-0.3  F200.0
X-22.01  F400.0
Z-0.6  F200.0
X22.01  F400.0
Z-0.9  F200.0
X-22.01  F400.0
Z-1.2  F200.0
X22.01  F400.0
Z-1.5  F200.0
X-22.01  F400.0
Z-1.8  F200.0
X22.01  F400.0
Z-2  F200.0
X-22.01  F400.0
G00 Z12

X-22.43 Y-185.4
G01 Z0.5  F300.0
Z-0.0  F200.0
X22.43  F400.0
Z-0.3  F200.0
X-22.43  F400.0
Z-0.6  F200.0
X22.43  F400.0
Z-0.9  F200.0
X-22.43  F400.0
Z-1.2  F200.0
X22.43  F400.0
Z-1.5  F200.0
X-22.43  F400.0
Z-1.8  F200.0
X22.43  F400.0
Z-2  F200.0
X-22.43  F400.0
G00 Z12

X-22.83 Y-210.52
G01 Z0.5  F300.0
Z-0.0  F200.0
X22.83  F400.0
Z-0.3  F200.0
X-22.83  F400.0
Z-0.6  F200.0
X22.83  F400.0
Z-0.9  F200.0
X-22.83  F400.0
Z-1.2  F200.0
X22.83  F400.0
Z-1.5  F200.0
X-22.83  F400.0
Z-1.8  F200.0
X22.83  F400.0
Z-2  F200.0
X-22.83  F400.0
G00 Z12

G00 X0 Y0
M5 M9
M30
(FILE 1 ENDS HERE)










(FILE 2 STARTS HERE)
G00 G49 G40.1 G17 G80 G50 G90
G21
(Fingerboard guitare folk)
(Milling  Frets 7 to 14)
(Please set the 0,0,0 point to the center of Fret 7, at the surface of the Fretboard blank)
(Y axis is the scale axis, milling will be done towards the negative Y direction)

M6 T5
M03 S10000
G00 Z12


X-22.83 Y0.0
G01 Z0.5  F300.0
Z-0.0  F200.0
X22.83  F400.0
Z-0.3  F200.0
X-22.83  F400.0
Z-0.6  F200.0
X22.83  F400.0
Z-0.9  F200.0
X-22.83  F400.0
Z-1.2  F200.0
X22.83  F400.0
Z-1.5  F200.0
X-22.83  F400.0
Z-1.8  F200.0
X22.83  F400.0
Z-2  F200.0
X-22.83  F400.0
G00 Z12

X-23.2 Y-23.71
G01 Z0.5  F300.0
Z-0.0  F200.0
X23.2  F400.0
Z-0.3  F200.0
X-23.2  F400.0
Z-0.6  F200.0
X23.2  F400.0
Z-0.9  F200.0
X-23.2  F400.0
Z-1.2  F200.0
X23.2  F400.0
Z-1.5  F200.0
X-23.2  F400.0
Z-1.8  F200.0
X23.2  F400.0
Z-2  F200.0
X-23.2  F400.0
G00 Z12

X-23.55 Y-46.09
G01 Z0.5  F300.0
Z-0.0  F200.0
X23.55  F400.0
Z-0.3  F200.0
X-23.55  F400.0
Z-0.6  F200.0
X23.55  F400.0
Z-0.9  F200.0
X-23.55  F400.0
Z-1.2  F200.0
X23.55  F400.0
Z-1.5  F200.0
X-23.55  F400.0
Z-1.8  F200.0
X23.55  F400.0
Z-2  F200.0
X-23.55  F400.0
G00 Z12

X-23.89 Y-67.22
G01 Z0.5  F300.0
Z-0.0  F200.0
X23.89  F400.0
Z-0.3  F200.0
X-23.89  F400.0
Z-0.6  F200.0
X23.89  F400.0
Z-0.9  F200.0
X-23.89  F400.0
Z-1.2  F200.0
X23.89  F400.0
Z-1.5  F200.0
X-23.89  F400.0
Z-1.8  F200.0
X23.89  F400.0
Z-2  F200.0
X-23.89  F400.0
G00 Z12

X-24.2 Y-87.16
G01 Z0.5  F300.0
Z-0.0  F200.0
X24.2  F400.0
Z-0.3  F200.0
X-24.2  F400.0
Z-0.6  F200.0
X24.2  F400.0
Z-0.9  F200.0
X-24.2  F400.0
Z-1.2  F200.0
X24.2  F400.0
Z-1.5  F200.0
X-24.2  F400.0
Z-1.8  F200.0
X24.2  F400.0
Z-2  F200.0
X-24.2  F400.0
G00 Z12

X-24.5 Y-105.98
G01 Z0.5  F300.0
Z-0.0  F200.0
X24.5  F400.0
Z-0.3  F200.0
X-24.5  F400.0
Z-0.6  F200.0
X24.5  F400.0
Z-0.9  F200.0
X-24.5  F400.0
Z-1.2  F200.0
X24.5  F400.0
Z-1.5  F200.0
X-24.5  F400.0
Z-1.8  F200.0
X24.5  F400.0
Z-2  F200.0
X-24.5  F400.0
G00 Z12

X-24.78 Y-123.74
G01 Z0.5  F300.0
Z-0.0  F200.0
X24.78  F400.0
Z-0.3  F200.0
X-24.78  F400.0
Z-0.6  F200.0
X24.78  F400.0
Z-0.9  F200.0
X-24.78  F400.0
Z-1.2  F200.0
X24.78  F400.0
Z-1.5  F200.0
X-24.78  F400.0
Z-1.8  F200.0
X24.78  F400.0
Z-2  F200.0
X-24.78  F400.0
G00 Z12

X-25.05 Y-140.51
G01 Z0.5  F300.0
Z-0.0  F200.0
X25.05  F400.0
Z-0.3  F200.0
X-25.05  F400.0
Z-0.6  F200.0
X25.05  F400.0
Z-0.9  F200.0
X-25.05  F400.0
Z-1.2  F200.0
X25.05  F400.0
Z-1.5  F200.0
X-25.05  F400.0
Z-1.8  F200.0
X25.05  F400.0
Z-2  F200.0
X-25.05  F400.0
G00 Z12

G00 X0 Y0
M5 M9
M30
(FILE 2 ENDS HERE)










(FILE 3 STARTS HERE)
G00 G49 G40.1 G17 G80 G50 G90
G21
(Fingerboard guitare folk)
(Milling  Frets 14 to 20)
(Please set the 0,0,0 point to the center of Fret 14, at the surface of the Fretboard blank)
(Y axis is the scale axis, milling will be done towards the negative Y direction)

M6 T5
M03 S10000
G00 Z12


X-25.05 Y0.0
G01 Z0.5  F300.0
Z-0.0  F200.0
X25.05  F400.0
Z-0.3  F200.0
X-25.05  F400.0
Z-0.6  F200.0
X25.05  F400.0
Z-0.9  F200.0
X-25.05  F400.0
Z-1.2  F200.0
X25.05  F400.0
Z-1.5  F200.0
X-25.05  F400.0
Z-1.8  F200.0
X25.05  F400.0
Z-2  F200.0
X-25.05  F400.0
G00 Z12

X-25.3 Y-15.83
G01 Z0.5  F300.0
Z-0.0  F200.0
X25.3  F400.0
Z-0.3  F200.0
X-25.3  F400.0
Z-0.6  F200.0
X25.3  F400.0
Z-0.9  F200.0
X-25.3  F400.0
Z-1.2  F200.0
X25.3  F400.0
Z-1.5  F200.0
X-25.3  F400.0
Z-1.8  F200.0
X25.3  F400.0
Z-2  F200.0
X-25.3  F400.0
G00 Z12

X-25.53 Y-30.76
G01 Z0.5  F300.0
Z-0.0  F200.0
X25.53  F400.0
Z-0.3  F200.0
X-25.53  F400.0
Z-0.6  F200.0
X25.53  F400.0
Z-0.9  F200.0
X-25.53  F400.0
Z-1.2  F200.0
X25.53  F400.0
Z-1.5  F200.0
X-25.53  F400.0
Z-1.8  F200.0
X25.53  F400.0
Z-2  F200.0
X-25.53  F400.0
G00 Z12

X-25.75 Y-44.86
G01 Z0.5  F300.0
Z-0.0  F200.0
X25.75  F400.0
Z-0.3  F200.0
X-25.75  F400.0
Z-0.6  F200.0
X25.75  F400.0
Z-0.9  F200.0
X-25.75  F400.0
Z-1.2  F200.0
X25.75  F400.0
Z-1.5  F200.0
X-25.75  F400.0
Z-1.8  F200.0
X25.75  F400.0
Z-2  F200.0
X-25.75  F400.0
G00 Z12

X-25.96 Y-58.17
G01 Z0.5  F300.0
Z-0.0  F200.0
X25.96  F400.0
Z-0.3  F200.0
X-25.96  F400.0
Z-0.6  F200.0
X25.96  F400.0
Z-0.9  F200.0
X-25.96  F400.0
Z-1.2  F200.0
X25.96  F400.0
Z-1.5  F200.0
X-25.96  F400.0
Z-1.8  F200.0
X25.96  F400.0
Z-2  F200.0
X-25.96  F400.0
G00 Z12

X-26.16 Y-70.73
G01 Z0.5  F300.0
Z-0.0  F200.0
X26.16  F400.0
Z-0.3  F200.0
X-26.16  F400.0
Z-0.6  F200.0
X26.16  F400.0
Z-0.9  F200.0
X-26.16  F400.0
Z-1.2  F200.0
X26.16  F400.0
Z-1.5  F200.0
X-26.16  F400.0
Z-1.8  F200.0
X26.16  F400.0
Z-2  F200.0
X-26.16  F400.0
G00 Z12

X-26.35 Y-82.59
G01 Z0.5  F300.0
Z-0.0  F200.0
X26.35  F400.0
Z-0.3  F200.0
X-26.35  F400.0
Z-0.6  F200.0
X26.35  F400.0
Z-0.9  F200.0
X-26.35  F400.0
Z-1.2  F200.0
X26.35  F400.0
Z-1.5  F200.0
X-26.35  F400.0
Z-1.8  F200.0
X26.35  F400.0
Z-2  F200.0
X-26.35  F400.0
G00 Z12

G00 X0 Y0
M5 M9
M30
(FILE 3 ENDS HERE)


```
