# Kick mappings
KICK_MAPPINGS = {
    'C1': 'C0',  # kick
    'B0': 'C0',  # kick
    'A#0': 'C0',  # kick
}

# Snare mappings
SNARE_MAPPINGS = {
    'D1': 'D0',  # snare center
    'D#1': 'D0',  # snare center
    'E1': 'D0',  # snare center
}

# Hi-hat mappings
HIHAT_MAPPINGS = {
    'B-2': 'G1',  # hi-hat closed tip
    'F#1': 'G1',  # hi-hat closed tip
    'A#-2': 'C2',  # hi-hat pedal
    'A-1': 'C2',  # hi-hat pedal
    'G#1': 'C2',  # hi-hat pedal
    'E3': 'G1',  # hi-hat closed tip
    'D8': 'G1',  # hi-hat closed tip
    'D#3': 'F1',  # hi-hat tight tip
    'D3': 'F#1',  # hi-hat closed tip
    'C0': 'B1',  # hi-hat open
    'C#0': 'B1',  # hi-hat open
    'D0': 'B1',  # hi-hat open
    'C8': 'B1',  # hi-hat open
    'D#8': 'B1',  # hi-hat open
    'C#8': 'B1',  # hi-hat open
    'E8': 'B1',  # hi-hat open
    'C-1': 'B1',  # hi-hat open
    'C#-1': 'B1',  # hi-hat open
    'D-1': 'B1',  # hi-hat open
    'D#-1': 'B1',  # hi-hat open
    'E-1': 'B1',  # hi-hat open
    'F-1': 'B1',  # hi-hat open,
    'A#-1': 'G1' #hi-hat closed tip
}

# Cymbal 1 mappings
CYMBAL1_MAPPINGS = {
    'G#0': 'G#2',  # crash 1 hit
    'G0': 'G#2',  # crash 1 hit
    'G2': 'G#2',  # crash 1 hit
    'G#2': 'A2',  # crash 1 mute
    'A#5': 'A2',  # crash 1 mute
}

# Cymbal 2 mappings
CYMBAL2_MAPPINGS = {
    'F#0': 'E2',  # crash 2 hit
    'F0': 'E2',  # crash 2 hit
    'C#2': 'E2',  # crash 2 hit
    'D2': 'F2',  # crash 2 mute
    'B5': 'F2',  # crash 2 mute
}

# Cymbal 3 mappings
CYMBAL3_MAPPINGS = {
    'A2': 'F#2',  # crash 3 hit
    'A#2': 'G2',  # crash 3 mute
    'A#6': 'G2',  # crash 3 mute
}

# China mappings
CHINA_MAPPINGS = {
    'D#0': 'F3',  # china hit
    'E0': 'F3',  # china hit
    'E2': 'F3',  # china hit
    'F#2': 'F#3',  # china mute
    'B6': 'F#3',  # china mute
}

# Ride mappings
RIDE_MAPPINGS = {
    'B2': 'D3',  # ride bow
    'D#2': 'D3',  # ride bow
    'A6': 'D3',  # ride bow
    'G#6': 'D3',  # ride bow
    'G6': 'D3',  # ride bow
    'F6': 'D3',  # ride bow
    'E6': 'D3',  # ride bow
    'D#6': 'D3',  # ride bow
    'D6': 'D3',  # ride bow
    'C6': 'D3',  # ride bow
    'A5': 'D3',  # ride bow
    'G#5': 'D3',  # ride bow
    'G5': 'D3',  # ride bow
    'F5': 'D3',  # ride bow
    'E5': 'D3',  # ride bow
    'D#5': 'D3',  # ride bow
    'D5': 'D3',  # ride bow
    'C5': 'D3',  # ride bow
    'B4': 'D3',  # ride bow
    'A#7': 'D3',  # ride bow
    'A7': 'D3',  # ride bow
    'G#7': 'D3',  # ride bow
    'G7': 'D3',  # ride bow
    'F7': 'D3',  # ride bow
    'E7': 'D3',  # ride bow
    'D#7': 'D3',  # ride bow
    'D7': 'D3',  # ride bow
    'C7': 'D3',  # ride bow
    'F2': 'C#3',  # ride bell
    'F#6': 'C#3',  # ride bell
    'C#6': 'C#3',  # ride bell
    'F#5': 'C#3',  # ride bell
    'C#5': 'C#3',  # ride bell
    'F#4': 'C#3',  # ride bell
    'C#7': 'C#3',  # ride bell
}
RACKTOM1_MAPPINGS = {
    'C2': 'A0',  # racktom 1
    'B1': 'A0',  # racktom 1
    'A4': 'A0',  # racktom 1
    'G4': 'A0',  # racktom 1
}

FLOORTOM1_MAPPINGS = {
    'A1': 'A#0',  # floortom 1
    'G1': 'A#0',  # floortom 1
    'F4': 'A#0',  # floortom 1
    'D4': 'A#0',  # floortom 1
}

FLOORTOM2_MAPPINGS = {
    'F1': 'B0',  # floortom 2
    'C4': 'B0',  # floortom 2
}

# Combine all mappings
NOTE_MAPPINGS = {
    **KICK_MAPPINGS,
    **SNARE_MAPPINGS,
    **HIHAT_MAPPINGS,
    **CYMBAL1_MAPPINGS,
    **CYMBAL2_MAPPINGS,
    **CYMBAL3_MAPPINGS,
    **CHINA_MAPPINGS,
    **RIDE_MAPPINGS,
    **RACKTOM1_MAPPINGS,
    **FLOORTOM1_MAPPINGS,
    **FLOORTOM2_MAPPINGS
}