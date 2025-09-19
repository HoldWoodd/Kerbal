import adjust
SE = 0.2
ADP = 0.5

def forward_10(vessel, flight, DEG = 2.8):
    PITCH = -10
    adjust.BFadjust(vessel, flight, DEG, PITCH, SE, ADP)

def forward_20(vessel, flight, DEG = 5):   
    PITCH = -20
    adjust.BFadjust(vessel, flight, DEG, PITCH, SE, ADP)

def backward_10(vessel, flight, DEG = 2.8):
    PITCH = 10
    adjust.BFadjust(vessel, flight, DEG, PITCH, SE, ADP)

def backward_20(vessel, flight, DEG = 5):   
    PITCH = 20
    adjust.BFadjust(vessel, flight, DEG, PITCH, SE, ADP)

def stop(vessel, flight, DEG = 5):   
    PITCH = 0
    adjust.BFadjust(vessel, flight, DEG, PITCH, SE, ADP)
    adjust.LRadjust(vessel, flight, DEG, PITCH, SE, ADP)

def up(vessel, DEG = 3):   
    adjust.heightadjust(vessel, DEG)

def down(vessel, DEG = -2):   
    adjust.heightadjust(vessel, DEG)