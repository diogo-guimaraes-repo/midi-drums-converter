import unittest
from src.converters.midi_converter import MidiConverter
from src.models.midi_file import MidiFile

class TestMidiConverter(unittest.TestCase):
    def test_convert_drum_bass(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'C1', 'velocity': 100, 'time': 0},  # kick
            {'note': 'B0', 'velocity': 100, 'time': 0},  # kick
            {'note': 'A#0', 'velocity': 100, 'time': 0}  # kick
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = ['C0', 'C0', 'C0']  # kick
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

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
            {'note': 'E8', 'velocity': 100, 'time': 0},
            {'note': 'C-1', 'velocity': 100, 'time': 0},
            {'note': 'C#-1', 'velocity': 100, 'time': 0},
            {'note': 'D-1', 'velocity': 100, 'time': 0},
            {'note': 'D#-1', 'velocity': 100, 'time': 0},
            {'note': 'E-1', 'velocity': 100, 'time': 0},
            {'note': 'F-1', 'velocity': 100, 'time': 0}
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = [
            'G1', 'G1', 'C2', 'C2', 'C2', 'G#1', 'G#1', 'F1', 'F#1', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1',
            'B1', 'B1', 'B1', 'B1', 'B1', 'B1'
        ]
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

    def test_convert_cymbal_1(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'G#0', 'velocity': 100, 'time': 0},  # crash 1 hit
            {'note': 'G0', 'velocity': 100, 'time': 0},   # crash 1 hit
            {'note': 'G2', 'velocity': 100, 'time': 0},   # crash 1 hit
            {'note': 'G#2', 'velocity': 100, 'time': 0},  # crash 1 mute
            {'note': 'A#5', 'velocity': 100, 'time': 0}   # crash 1 mute
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = ['G#2', 'G#2', 'G#2', 'A2', 'A2']  # crash 1 hit and mute
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

    def test_convert_cymbal_2(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'F#0', 'velocity': 100, 'time': 0},  # crash 2 hit
            {'note': 'F0', 'velocity': 100, 'time': 0},   # crash 2 hit
            {'note': 'C#2', 'velocity': 100, 'time': 0},  # crash 2 hit
            {'note': 'D2', 'velocity': 100, 'time': 0}    # crash 2 mute
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = ['E2', 'E2', 'E2', 'F2']  # crash 2 hit and mute
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

    def test_convert_cymbal_3(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'A2', 'velocity': 100, 'time': 0},   # crash 3 hit
            {'note': 'A#2', 'velocity': 100, 'time': 0},  # crash 3 mute
            {'note': 'A#6', 'velocity': 100, 'time': 0},  # crash 3 mute
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = ['F#2', 'G2', 'G2']  # crash 3 hit and mute
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

    def test_convert_ride(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'B2', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'D#2', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'A6', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'G#6', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'G6', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'F6', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'E6', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'D#6', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'D6', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'C6', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'A5', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'G#5', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'G5', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'F5', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'E5', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'D#5', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'D5', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'C5', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'B4', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'A#7', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'A7', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'G#7', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'G7', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'F7', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'E7', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'D#7', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'D7', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'C7', 'velocity': 100, 'time': 0},  # ride bow
            {'note': 'F2', 'velocity': 100, 'time': 0},  # ride bell
            {'note': 'F#6', 'velocity': 100, 'time': 0},  # ride bell
            {'note': 'C#6', 'velocity': 100, 'time': 0},  # ride bell
            {'note': 'F#5', 'velocity': 100, 'time': 0},  # ride bell
            {'note': 'C#5', 'velocity': 100, 'time': 0},  # ride bell
            {'note': 'F#4', 'velocity': 100, 'time': 0},  # ride bell
            {'note': 'C#7', 'velocity': 100, 'time': 0}  # ride bell
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = [
            'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'C#3', 'C#3', 'C#3', 'C#3', 'C#3', 'C#3', 'C#3'
        ]  # ride bow and bell
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

    def test_convert_china(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'D#0', 'velocity': 100, 'time': 0},  # china hit
            {'note': 'E0', 'velocity': 100, 'time': 0},   # china hit
            {'note': 'E2', 'velocity': 100, 'time': 0},   # china hit
            {'note': 'F#2', 'velocity': 100, 'time': 0},  # china mute
            {'note': 'B6', 'velocity': 100, 'time': 0}    # china mute
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = ['F3', 'F3', 'F3', 'F#3', 'F#3']  # china hit and mute
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

    def test_convert_racktom_1(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'C2', 'velocity': 100, 'time': 0},  # racktom 1
            {'note': 'B1', 'velocity': 100, 'time': 0},  # racktom 1
            {'note': 'A4', 'velocity': 100, 'time': 0},  # racktom 1
            {'note': 'G4', 'velocity': 100, 'time': 0}   # racktom 1
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = ['A0', 'A0', 'A0', 'A0']  # racktom 1
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

    def test_convert_floortom_1(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'A1', 'velocity': 100, 'time': 0},  # floortom 1
            {'note': 'G1', 'velocity': 100, 'time': 0},  # floortom 1
            {'note': 'F4', 'velocity': 100, 'time': 0},  # floortom 1
            {'note': 'D4', 'velocity': 100, 'time': 0}   # floortom 1
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = ['A#0', 'A#0', 'A#0', 'A#0']  # floortom 1
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])

    def test_convert_floortom_2(self):
        midi_file = MidiFile('/path/to/midi/file')
        converter = MidiConverter()

        midi_file.load = lambda: None
        midi_file.save = lambda: None

        midi_file.data = [
            {'note': 'F1', 'velocity': 100, 'time': 0},  # floortom 2
            {'note': 'C4', 'velocity': 100, 'time': 0}   # floortom 2
        ]

        converter.convert_to_pv(midi_file)
        expected_notes = ['B0', 'B0']  # floortom 2
        for i, note in enumerate(midi_file.data):
            self.assertEqual(note['note'], expected_notes[i])
if __name__ == '__main__':
    unittest.main()