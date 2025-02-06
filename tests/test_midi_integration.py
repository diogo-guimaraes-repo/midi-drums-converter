import unittest
import tempfile
import os
import subprocess
import mido
from src.models.midi_file import midi_note_to_name  # our custom helper function

class TestMidiIntegration(unittest.TestCase):
    def test_main_program_conversion(self):
        # Create a temporary input MIDI file.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_in:
            input_filename = temp_in.name

        # Create a temporary output MIDI file.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_out:
            output_filename = temp_out.name

        try:
            # Build a minimal MIDI file using mido.
            # For example, create a track with one note_on message:
            #   Use note number 24, which our helper should convert to "C1"
            #   According to your mappings, "C1" should be converted to "C0".
            mid = mido.MidiFile()
            track = mido.MidiTrack()
            mid.tracks.append(track)
            track.append(mido.Message('note_on', note=36, velocity=100, time=0))
            mid.save(input_filename)

            # Call your main program using subprocess.
            # (Assume your main program is in "convert_midi.py" in the working directory.)
            result = subprocess.run(
                ["python", "convert_midi.py", input_filename, output_filename],
                capture_output=True,
                text=True
            )
            # Ensure the program exited successfully.
            self.assertEqual(result.returncode, 0, msg=f"Program error: {result.stderr}")

            # Load the output MIDI file with mido.
            mid_converted = mido.MidiFile(output_filename)
            converted_note_names = []
            for track in mid_converted.tracks:
                for msg in track:
                    if msg.type == 'note_on':
                        # Use our custom helper function to convert the note number to a note name.
                        converted_note_names.append(midi_note_to_name(msg.note))

            # Verify that the conversion was applied.
            # For example, we expect "C1" to have been converted to "C0".
            self.assertIn("C0", converted_note_names, 
                          msg="Expected converted note 'C0' not found in output file.")

        finally:
            # Cleanup temporary files.
            os.remove(input_filename)
            os.remove(output_filename)

if __name__ == '__main__':
    unittest.main()
