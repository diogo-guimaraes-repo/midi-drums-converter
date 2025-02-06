#!/usr/bin/env python
import sys
from src.converters.midi_converter import MidiConverter
from src.models.midi_file import MidiFile

def main():
    if len(sys.argv) < 3:
        print("Usage: python convert_midi.py <input_file.mid> <output_file.mid>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Load the MIDI file.
    midi_file = MidiFile(input_file)
    midi_file.load()  # Implement this method to populate midi_file.data from the file.
    
    # Convert the MIDI data.
    converter = MidiConverter()
    converter.convert_to_pv(midi_file)
    
    # Save the converted MIDI file.
    midi_file.filename = output_file
    midi_file.save()  # Implement this method to write midi_file.data back into a MIDI file.
    
    print(f"Converted MIDI file saved to {output_file}")

if __name__ == '__main__':
    main()