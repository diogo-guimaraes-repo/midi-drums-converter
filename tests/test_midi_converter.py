import mido
import unittest
from src.converters.midi_converter import MidiConverter
from src.converters.note_mappings import NOTE_MAPPINGS

class TestMidiConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MidiConverter()

    def convert_note(self, note):
        """
        Given an integer note, convert it using the converter's logic:
        - Convert the integer note to its note name.
        - If that note name is in NOTE_MAPPINGS, get the mapped note name,
          convert that mapped name back to an integer, and return it.
        - Otherwise, return the original note.
        """
        nname = self.converter.midi_note_to_name(note)
        if nname in NOTE_MAPPINGS:
            return self.converter.note_name_to_int(NOTE_MAPPINGS[nname])
        else:
            return note
        
    def test_midi_note_to_name(self):
        # Test cases for midi_note_to_name function
        test_cases = [
           (0, 'C-2'),
           (12, 'C-1'),
           (24, 'C0'),
           (36, 'C1'),
           (48, 'C2'),
           (60, 'C3'),
           (72, 'C4'),
           (84, 'C5'),
           (96, 'C6'),
           (108, 'C7'),
           (120, 'C8'),
           (127, 'G8')
        ]

        for note_number, expected_name in test_cases:
            with self.subTest(note_number=note_number, expected_name=expected_name):
                self.assertEqual(self.converter.midi_note_to_name(note_number), expected_name)

    def test_convert_drum_bass(self):
        # Drum Bass: 36 = "C1", 35 = "B0", 34 = "A#0" – all should be mapped to "C0"
        input_notes = [36, 35, 34]
        expected_note_names = ["C0", "C0", "C0"]
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"Drum Bass: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")

    def test_convert_snare_drums(self):
        # Snare: 38 = "D1", 39 = "D#1", 40 = "E1" – all should be mapped to "D0"
        input_notes = [38, 39, 40]
        expected_note_names = ["D0", "D0", "D0"]
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"Snare: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")

    def test_convert_hi_hats(self):
        # Hi-Hats: input note integers (with inline comments indicating their note names)
        input_notes = [
            11,   # 11 → "B-2"
            42,   # 42 → "F#1"
            10,   # 10 → "A#-2"
            21,   # 21 → "A-1"
            44,   # 44 → "G#1"
            64,   # 64 → "E3"
            122,  # 122 → "D8"
            63,   # 63 → "D#3"
            62,   # 62 → "D3"
            24,   # 24 → "C0"
            25,   # 25 → "C#0"
            26,   # 26 → "D0"
            120,  # 120 → "C8"
            123,  # 123 → "D#8"
            121,  # 121 → "C#8"
            124,  # 124 → "E8"
            12,   # 12 → "C-1"
            13,   # 13 → "C#-1"
            14,   # 14 → "D-1"
            15,   # 15 → "D#-1"
            16,   # 16 → "E-1"
            17,    # 17 → "F-1"
            22,    # 17 → "F-1"
        ]
        # Expected mapping for hi-hats, according to your NOTE_MAPPINGS:
        expected_note_names = [
            'G1', 'G1', 'C2', 'C2', 'C2', 'G1', 'G1', 'F1', 'F#1', 
            'B1', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1', 
            'B1', 'B1', 'B1', 'G1'
        ]
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"Hi-hat: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")

    def test_convert_cymbal_1(self):
        # Cymbal 1: input note integers:
        # 32 → "G#0", 31 → "G0", 55 → "G2", 56 → "G#2", 94 → "A#5"
        input_notes = [32, 31, 55, 56, 94]
        # Expected mapping for cymbal 1: e.g. ['G#2', 'G#2', 'G#2', 'A2', 'A2']
        expected_note_names = ['G#2', 'G#2', 'G#2', 'A2', 'A2']
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"Cymbal 1: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")

    def test_convert_cymbal_2(self):
        # Cymbal 2: input note integers:
        # 30 → "F#0", 29 → "F0", 49 → "C#2", 50 → "D2"
        input_notes = [30, 29, 49, 50]
        # Expected mapping for cymbal 2: ['E2', 'E2', 'E2', 'F2']
        expected_note_names = ['E2', 'E2', 'E2', 'F2']
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"Cymbal 2: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")

    def test_convert_cymbal_3(self):
        # Cymbal 3: input note integers:
        # 57 → "A2", 58 → "A#2", 106 → "A#6"
        input_notes = [57, 58, 106]
        # Expected mapping for cymbal 3: ['F#2', 'G2', 'G2']
        expected_note_names = ['F#2', 'G2', 'G2']
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"Cymbal 3: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")

    def test_convert_ride(self):
        # Ride: input note integers:
        # 59 → "B2", 51 → "D#2", 105 → "A6", 104 → "G#6", 103 → "G6",
        # 101 → "F6", 100 → "E6", 99 → "D#6", 98 → "D6", 96 → "C6",
        # 93 → "A5", 92 → "G#5", 91 → "G5", 89 → "F5", 88 → "E5",
        # 87 → "D#5", 86 → "D5", 84 → "C5", 83 → "B4", 118 → "A#7",
        # 117 → "A7", 116 → "G#7", 115 → "G7", 113 → "F7", 112 → "E7",
        # 111 → "D#7", 110 → "D7", 108 → "C7",
        # 53 → "F2" (corrected), 102 → "F#6", 97 → "C#6", 90 → "F#5",
        # 85 → "C#5", 78 → "F#4", 109 → "C#7"
        input_notes = [
            59, 51, 105, 104, 103, 101, 100, 99, 98, 96,
            93, 92, 91, 89, 88, 87, 86, 84, 83, 118,
            117, 116, 115, 113, 112, 111, 110, 108,
            53, 102, 97, 90, 85, 78, 109
        ]
        # Expected mapping for ride:
        # Instead of computing a long aggregated list, here we directly supply the expected note names array:
        expected_note_names = [
            # For this example, suppose the expected conversion is as follows:
            # (You can adjust these expected values as needed based on your NOTE_MAPPINGS.)
            'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3',
            'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3',
            'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3',
            'C#3', 'C#3', 'C#3', 'C#3', 'C#3', 'C#3', 'C#3'
        ]
        expected_ints = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_ints):
            converted = self.convert_note(note)
            self.assertEqual(
                converted, exp,
                f"Ride: input {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}"
            )

    def test_convert_china(self):
        # China: input note integers:
        # 15 → "D#0", 16 → "E0", 52 → "E2", 54 → "F#2", 107 → "B6"
        input_notes = [27, 28, 52, 54, 107]
        # Expected conversion for china: ['F3', 'F3', 'F3', 'F#3', 'F#3']
        expected_note_names = ['F3', 'F3', 'F3', 'F#3', 'F#3']
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"China: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")

    def test_convert_racktom_1(self):
        # Racktom 1: input note integers:
        # 48 → "C2", 47 → "B1", 81 → "A4", 79 → "G4"
        input_notes = [48, 47, 81, 79]
        # Expected mapping for racktom 1: all should become "A0"
        expected_note_names = ["A0"] * 4
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"Racktom 1: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")

    def test_convert_floortom_1(self):
        # Floortom 1: input note integers:
        # 45 → "A1", 43 → "G1", 77 → "F4", 74 → "D4"
        input_notes = [45, 43, 77, 74]
        # Expected conversion for floortom 1: all should become "A#0"
        expected_note_names = ["A#0"] * 4
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"Floortom 1: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")

    def test_convert_floortom_2(self):
        # Floortom 2: input note integers:
        # 41 → "F1", 60 → "C4"
        input_notes = [41, 72]
        # Expected conversion for floortom 2: both should become "B0"
        expected_note_names = ["B0", "B0"]
        expected_notes = [self.converter.note_name_to_int(n) for n in expected_note_names]
        for note, exp in zip(input_notes, expected_notes):
            converted = self.convert_note(note)
            self.assertEqual(converted, exp,
                             f"Floortom 2: {note} ({self.converter.midi_note_to_name(note)}) should convert to {exp} but got {converted}")


if __name__ == '__main__':
    unittest.main()