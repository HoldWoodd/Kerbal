from setor import set_deg_by_id

def BFadjust(vessel, flight, DEG, PITCH, SE, ADP):
        if flight.pitch > PITCH + SE:
            set_deg_by_id(vessel, "F", DEG - (flight.pitch - PITCH - SE)/5 * ADP)
            set_deg_by_id(vessel, "B", DEG + (flight.pitch - PITCH - SE)/5 * ADP)
        elif flight.pitch < PITCH - SE:
            set_deg_by_id(vessel, "B", DEG - (PITCH - SE - flight.pitch)/5 * ADP)
            set_deg_by_id(vessel, "F", DEG + (PITCH - SE - flight.pitch)/5 * ADP)
        else:
            set_deg_by_id(vessel, "F", DEG)
            set_deg_by_id(vessel, "B", DEG)

def LRadjust(vessel, flight, DEG, ROLL, SE, ADP):
        if flight.roll > ROLL + SE:
            set_deg_by_id(vessel, "L", DEG - (flight.roll - ROLL - SE)/5 * ADP)
            set_deg_by_id(vessel, "R", DEG + (flight.roll - ROLL - SE)/5 * ADP)
        elif flight.roll < ROLL - SE:
            set_deg_by_id(vessel, "R", DEG - (ROLL - SE - flight.roll)/5 * ADP)
            set_deg_by_id(vessel, "L", DEG + (ROLL - SE - flight.roll)/5 * ADP)
        else:
            set_deg_by_id(vessel, "L", DEG)
            set_deg_by_id(vessel, "R", DEG)

def heightadjust(vessel, DEG):
        set_deg_by_id(vessel, "B", DEG)
        set_deg_by_id(vessel, "F", DEG)