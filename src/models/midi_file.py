# src/models/midi_file.py
import mido

def midi_note_to_name(note):
    """
    Convert a MIDI note number (0-127) to its note name.
    For example, 60 becomes 'C4', 61 becomes 'C#4', etc.
    """
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = note // 12 - 2
    name = note_names[note % 12]
    return f"{name}{octave}"

class MidiFile:
    def __init__(self, filename):
        self.filename = filename
        # This list will hold note event dictionaries, e.g., {'note': 'C1', 'velocity': 100, 'time': 0}
        self.data = []

    def load(self):
        """
        Load the MIDI file from self.filename and populate self.data with note events.
        Each note event is stored as a dictionary containing:
          - 'note': a string (e.g., 'C1')
          - 'velocity': the MIDI velocity value (int)
          - 'time': the delta time (int)
        """
        mid = mido.MidiFile(self.filename)
        self.data = []

        # Iterate through all tracks and messages.
        for track in mid.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    # Convert the MIDI note number to a note name using our helper function.
                    note_name = midi_note_to_name(msg.note)
                    self.data.append({
                        'note': note_name,
                        'velocity': msg.velocity,
                        'time': msg.time
                    })

    def save(self):
        """
        Save the contents of self.data to a new MIDI file at self.filename.
        This creates a new MIDI file with a single track, converting each note event back into a note_on message.
        """
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)

        for event in self.data:
            note_name = event.get('note', '')
            # Convert the note name back to a MIDI note number.
            note_int = self.note_name_to_int(note_name)
            msg = mido.Message(
                'note_on',
                note=note_int,
                velocity=event.get('velocity', 64),
                time=event.get('time', 0)
            )
            track.append(msg)

        mid.save(self.filename)

    def note_name_to_int(self, note_name):
        """
        Convert a note name (e.g., 'C1') to a MIDI note number.
        This implementation iterates over the valid MIDI note range (0-127)
        and returns the first note number that matches the given note name using midi_note_to_name().
        If no match is found, it returns 60 (middle C) as a default.
        """
        for i in range(0, 128):
            if midi_note_to_name(i) == note_name:
                return i
        return 60  # default fallback to middle C
