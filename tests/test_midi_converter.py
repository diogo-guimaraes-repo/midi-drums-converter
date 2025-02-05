import unittest
from src.converters.midi_converter import MidiConverter
from src.models.midi_file import MidiFile

class TestMidiConverter(unittest.TestCase):
    def test_convert_drum_bass(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [{'note': 'C1', 'velocity': 100, 'time': 0}]

        converter.convert_to_pv(midi_file)
        self.assertEqual(midi_file.data[0]['note'], 'C0')

    def test_convert_snare_drums(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'D1', 'velocity': 100, 'time': 0},
            {'note': 'D#1', 'velocity': 100, 'time': 0},
            {'note': 'E1', 'velocity': 100, 'time': 0}
        ]

        converter.convert_to_pv(midi_file)
        for note in midi_file.data:
            self.assertEqual(note['note'], 'D0')

    def test_convert_hi_hats(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'B-2', 'velocity': 100, 'time': 0},
            {'note': 'F#1', 'velocity': 100, 'time': 0},
            {'note': 'A#-2', 'velocity': 100, 'time': 0},
            {'note': 'A-1', 'velocity': 100, 'time': 0},
            {'note': 'G#1', 'velocity': 100, 'time': 0},
            {'note': 'E3', 'velocity': 100, 'time': 0},
            {'note': 'D8', 'velocity': 100, 'time': 0},
            {'note': 'D#3', 'velocity': 100, 'time': 0},
            {'note': 'D3', 'velocity': 100, 'time': 0},
            {'note': 'C0', 'velocity': 100, 'time': 0},
            {'note': 'C#0', 'velocity': 100, 'time': 0},
            {'note': 'D0', 'velocity': 100, 'time': 0},
            {'note': 'C8', 'velocity': 100, 'time': 0},
            {'note': 'D#8', 'velocity': 100, 'time': 0},
            {'note': 'C#8', 'velocity': 100, 'time': 0},
            {'note': 'E8', 'velocity': 100, 'time': 0}
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = [
            'G1', 'G1', 'C2', 'C2', 'C2', 'G#1', 'G#1', 'F1', 'F#1', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1'
        ]
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

if __name__ == '__main__':
    unittest.main()