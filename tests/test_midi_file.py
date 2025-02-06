import unittest
from src.models.midi_file import midi_note_to_name

class TestMidiFile(unittest.TestCase):
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
                self.assertEqual(midi_note_to_name(note_number), expected_name)

if __name__ == '__main__':
    unittest.main()