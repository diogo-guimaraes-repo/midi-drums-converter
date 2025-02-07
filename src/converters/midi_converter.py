import mido
from .note_mappings import NOTE_MAPPINGS

class MidiConverter:
    def convert_to_pv(self, input_path, output_path):
        midi_file = mido.MidiFile(input_path)
        for track in midi_file.tracks:
            for msg in track:
                if msg.type in ['note_on', 'note_off']:
                    note_name = self.midi_note_to_name(msg.note)
                    if note_name in NOTE_MAPPINGS:
                        msg.note = self.note_name_to_int(NOTE_MAPPINGS[note_name])
        midi_file.save(output_path)

    def midi_note_to_name(self, note):
        """
        Convert a MIDI note number (0-127) to its note name.
        For example, 60 becomes 'C4', 61 becomes 'C#4', etc.
        """
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        octave = note // 12 - 2
        name = note_names[note % 12]
        return f"{name}{octave}"



    def note_name_to_int(self, note_name):
        """
        Convert a note name (e.g., 'C1') to a MIDI note number.
        This implementation iterates over the valid MIDI note range (0-127)
        and returns the first note number that matches the given note name using midi_note_to_name().
        If no match is found, it returns 60 (middle C) as a default.
        """
        for i in range(0, 128):
            if self.midi_note_to_name(i) == note_name:
                return i
        return 60  # default fallback to middle C
