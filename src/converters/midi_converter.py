from .note_mappings import NOTE_MAPPINGS

class MidiConverter:
    def convert_to_pv(self, midi_file):
        for note in midi_file.data:
           if note['note'] in NOTE_MAPPINGS:
                note['note'] = NOTE_MAPPINGS[note['note']]