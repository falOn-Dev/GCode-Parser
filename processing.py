def handle_arguement(key, number):
    if key == "X":
        print(f"Moving along the X axis to {number}")
    elif key == "Y":
        print(f"Moving along the Y axis to {number}")
    elif key == "Z":
        print(f"Moving along the Z axis to {number}")
    elif key == "F":
        print(f"Setting the feedrate to {number}")
    elif key == "E":
        print(f"Extruding filament by {number}mm")