def set_deg_by_id(vessel, id, deg):
    for cs in vessel.parts.all:
        tag = None
        for md in cs.modules:
            if md.name == "KOSNameTag":
                tag = md.get_field("name tag") or ""
                break

        if not tag or id not in tag:
            continue
        
        for md in cs.modules:
            if md.name == "ModuleControlSurface":
                md.set_field_float("偏转角度", deg)